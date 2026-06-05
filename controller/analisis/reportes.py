import json
from datetime import datetime
from controller.utils.logger import get_logger

logger = get_logger(__name__)

def generar_reporte(resultado: dict) -> str:
    reporte = {
        "generado_en": datetime.now().isoformat(),
        "contrato_id": resultado.get("contrato_id"),
        "nombre":      resultado.get("nombre"),
        "resumen":     resultado.get("estadisticas"),
        "hallazgos":   resultado.get("hallazgos"),
    }
    logger.info(f"Reporte generado para contrato {resultado.get('contrato_id')}")
    return json.dumps(reporte, ensure_ascii=False, indent=2)
