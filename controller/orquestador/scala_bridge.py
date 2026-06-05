import subprocess
import json
from controller.utils.config import SCALA_JAR
from controller.utils.logger import get_logger

logger = get_logger(__name__)

def tokenizar_contrato(texto: str, contrato_id: str, nombre: str) -> dict:
    if not SCALA_JAR.exists():
        raise FileNotFoundError(
            f"JAR de Scala no encontrado en {SCALA_JAR}. "
            "Compila primero con: cd model/scala && sbt assembly"
        )
    resultado = subprocess.run(
        ["java", "-jar", str(SCALA_JAR), contrato_id, nombre],
        input=texto,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if resultado.returncode != 0:
        logger.error(f"Scala error: {resultado.stderr}")
        raise RuntimeError(f"Error en Scala: {resultado.stderr}")
    return json.loads(resultado.stdout)
