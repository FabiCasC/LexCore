import uuid
from datetime import datetime
from controller.orquestador.scala_bridge      import tokenizar_contrato
from controller.orquestador.prolog_bridge     import validar_clausulas
from controller.analisis.estadisticas         import calcular_estadisticas
from controller.almacenamiento.lector_json    import guardar_contrato_procesado
from controller.almacenamiento.lector_csv     import guardar_hallazgos, guardar_auditoria
from controller.utils.logger                  import get_logger

logger = get_logger(__name__)

def analizar_contrato(texto: str, nombre: str) -> dict:
    contrato_id = str(uuid.uuid4())[:8]
    logger.info(f"Iniciando análisis del contrato '{nombre}' [{contrato_id}]")

    contrato    = tokenizar_contrato(texto, contrato_id, nombre)
    hallazgos   = validar_clausulas(contrato["clausulas"])
    estadisticas = calcular_estadisticas(contrato["clausulas"], hallazgos)

    guardar_contrato_procesado(contrato)
    guardar_hallazgos(contrato_id, hallazgos)
    guardar_auditoria({
        "auditoria_id":     str(uuid.uuid4())[:8],
        "contrato_id":      contrato_id,
        "fecha":            datetime.now().isoformat(),
        "total_clausulas":  len(contrato["clausulas"]),
        "clausulas_riesgo": len(hallazgos),
        "resultado":        "con_riesgos" if hallazgos else "aprobado",
    })

    return {
        "contrato_id":  contrato_id,
        "nombre":       nombre,
        "clausulas":    contrato["clausulas"],
        "hallazgos":    hallazgos,
        "estadisticas": estadisticas,
    }
