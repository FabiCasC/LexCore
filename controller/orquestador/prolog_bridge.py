from pyswip import Prolog
from controller.utils.config import PROLOG_DIR
from controller.utils.logger import get_logger

logger = get_logger(__name__)

def validar_clausulas(clausulas: list[dict]) -> list[dict]:
    prolog = Prolog()
    prolog.consult(str(PROLOG_DIR / "base_conocimiento" / "hechos.pl"))
    prolog.consult(str(PROLOG_DIR / "base_conocimiento" / "reglas_generales.pl"))
    prolog.consult(str(PROLOG_DIR / "consultas"         / "validar_clausula.pl"))

    for c in clausulas:
        texto_atom = str(c["texto"]).replace("'", "\\'")
        prolog.assertz(f'clausula({c["id"]}, {c["tipo"]}, \'{texto_atom}\')')

    hallazgos = [
        {
            "clausula_id": int(sol["Id"]),
            "tipo_riesgo": str(sol["Tipo"]),
            "severidad":   str(sol["Severidad"]),
        }
        for sol in prolog.query("clausula_riesgosa(Id, Tipo, Severidad)")
    ]
    logger.info(f"Prolog encontró {len(hallazgos)} hallazgos")
    return hallazgos
