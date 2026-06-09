import pandas as pd
from controller.utils.config import HALLAZGOS_CSV, AUDITORIAS_CSV
from controller.utils.logger import get_logger

logger = get_logger(__name__)

def leer_hallazgos() -> pd.DataFrame:
    if not HALLAZGOS_CSV.exists():
        return pd.DataFrame(columns=["contrato_id", "clausula_id", "tipo_riesgo", "severidad", "fecha"])
    return pd.read_csv(HALLAZGOS_CSV)

def guardar_hallazgos(contrato_id: str, hallazgos: list[dict]) -> None:
    if not hallazgos:
        return
    df = pd.DataFrame(hallazgos)
    df["contrato_id"] = contrato_id
    df.to_csv(HALLAZGOS_CSV, mode="a", header=not HALLAZGOS_CSV.exists(), index=False)

def leer_auditorias() -> pd.DataFrame:
    if not AUDITORIAS_CSV.exists():
        return pd.DataFrame(columns=["auditoria_id", "contrato_id", "fecha", "total_clausulas", "clausulas_riesgo", "resultado"])
    return pd.read_csv(AUDITORIAS_CSV)

def guardar_auditoria(auditoria: dict) -> None:
    df = pd.DataFrame([auditoria])
    df.to_csv(AUDITORIAS_CSV, mode="a", header=not AUDITORIAS_CSV.exists(), index=False)
    logger.info(f"Auditoría {auditoria.get('auditoria_id')} guardada")
