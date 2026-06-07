import json
from controller.utils.config import CONTRATOS_RAW, CONTRATOS_PROC
from controller.utils.logger import get_logger

logger = get_logger(__name__)

def leer_contratos_raw() -> list[dict]:
    if not CONTRATOS_RAW.exists():
        return []
    with open(CONTRATOS_RAW, encoding="utf-8") as f:
        return json.load(f)

def guardar_contrato_procesado(contrato: dict) -> None:
    datos: list[dict] = []
    if CONTRATOS_PROC.exists():
        with open(CONTRATOS_PROC, encoding="utf-8") as f:
            datos = json.load(f)
    datos.append(contrato)
    with open(CONTRATOS_PROC, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    logger.info(f"Contrato {contrato.get('contrato_id')} guardado")
