import uuid
from datetime import datetime
from controller.orquestador.scala_bridge      import tokenizar_contrato
from controller.orquestador.prolog_bridge     import validar_clausulas
from controller.analisis.estadisticas         import calcular_estadisticas
from controller.almacenamiento.lector_json    import guardar_contrato_procesado
from controller.almacenamiento.lector_csv     import guardar_hallazgos, guardar_auditoria
from controller.utils.logger                  import get_logger
from model.python.modelos.contrato            import Contrato, Dictamen
from model.python.analisis.analizador         import calcular_perfil_estadistico

logger = get_logger(__name__)

def analizar_contrato(texto: str, nombre: str, categoria: str = "general") -> dict:
    contrato_id = str(uuid.uuid4())[:8]
    logger.info(f"Iniciando análisis del contrato '{nombre}' [{contrato_id}] categoria={categoria}")

    scala_output  = tokenizar_contrato(texto, contrato_id, nombre)
    hallazgos     = validar_clausulas(scala_output["clausulas"])
    estadisticas  = calcular_estadisticas(scala_output["clausulas"], hallazgos)

    # Construir modelo de dominio
    contrato_obj = Contrato(
        contrato_id=contrato_id,
        nombre=nombre,
        categoria=categoria,
        texto_original=texto,
    )
    contrato_obj.cargar_desde_scala(scala_output, hallazgos)

    clausulas_evaluadas = [c.evaluar() for c in contrato_obj.clausulas]
    perfil = calcular_perfil_estadistico(clausulas_evaluadas)
    dictamen = Dictamen(contrato=contrato_obj, estadisticas=perfil)
    resumen_dictamen = dictamen.resumen()

    guardar_contrato_procesado(scala_output)
    guardar_hallazgos(contrato_id, hallazgos)
    guardar_auditoria({
        "auditoria_id":     str(uuid.uuid4())[:8],
        "contrato_id":      contrato_id,
        "fecha":            datetime.now().isoformat(),
        "total_clausulas":  len(scala_output["clausulas"]),
        "clausulas_riesgo": len(hallazgos),
        "resultado":        "con_riesgos" if hallazgos else "aprobado",
        "score":            resumen_dictamen["score"],
        "nivel_riesgo":     resumen_dictamen["nivel_riesgo"],
    })

    return {
        "contrato_id":         contrato_id,
        "nombre":              nombre,
        "categoria":           categoria,
        "clausulas":           scala_output["clausulas"],
        "hallazgos":           hallazgos,
        "estadisticas":        estadisticas,
        "perfil":              perfil,
        "score":               resumen_dictamen["score"],
        "nivel_riesgo":        resumen_dictamen["nivel_riesgo"],
        "recomendacion_final": resumen_dictamen["recomendacion_final"],
    }
