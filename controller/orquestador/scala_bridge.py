import subprocess
import json
from pathlib import Path
from controller.utils.config import SCALA_JAR
from controller.utils.logger import get_logger

logger = get_logger(__name__)


def _build_jar_if_missing(jar_path: Path) -> None:
    scala_dir = jar_path.parent.parent.parent
    if jar_path.exists():
        return
    logger.info(f"JAR de Scala no encontrado en {jar_path}, ejecutando 'sbt assembly' en {scala_dir}")
    proc = subprocess.run(
        ["sbt", "assembly"],
        cwd=str(scala_dir),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        logger.error("Fallo al compilar el JAR de Scala")
        logger.error(proc.stdout)
        logger.error(proc.stderr)
        raise RuntimeError(f"No se pudo construir el JAR de Scala: {proc.stderr}")


def tokenizar_contrato(texto: str, contrato_id: str, nombre: str) -> dict:
    _build_jar_if_missing(SCALA_JAR)
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
    try:
        return json.loads(resultado.stdout)
    except json.JSONDecodeError as e:
        logger.error("Salida de Scala no es JSON válido")
        logger.error(resultado.stdout)
        raise
