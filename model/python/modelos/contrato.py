from datetime import datetime
from typing import List
from model.python.modelos.clausula import Clausula, fabricar_clausula


class Contrato:
    def __init__(self, contrato_id: str, nombre: str, categoria: str, texto_original: str):
        self.contrato_id = contrato_id
        self.nombre = nombre
        self.categoria = categoria
        self.texto_original = texto_original
        self.fecha_analisis = datetime.now().isoformat()
        self.clausulas: List[Clausula] = []

    def agregar_clausula(self, id: str, tipo: str, texto: str, severidad: str) -> Clausula:
        clausula = fabricar_clausula(
            categoria=self.categoria,
            id=id,
            tipo=tipo,
            texto=texto,
            severidad=severidad,
        )
        self.clausulas.append(clausula)
        return clausula

    def cargar_desde_scala(self, scala_output: dict, hallazgos_prolog: list) -> None:
        # Construir mapa de severidades desde los hallazgos de Prolog
        mapa_severidad = {}
        for h in hallazgos_prolog:
            clausula_id = h.get("clausula_id") or h.get("id", "")
            severidad = h.get("severidad", "medio")
            if clausula_id:
                mapa_severidad[clausula_id] = severidad

        for cl in scala_output.get("clausulas", []):
            cid = cl.get("id", "")
            self.agregar_clausula(
                id=cid,
                tipo=cl.get("tipo", "general"),
                texto=cl.get("texto", ""),
                severidad=mapa_severidad.get(cid, "bajo"),
            )

    def clausulas_riesgosas(self) -> List[Clausula]:
        return [c for c in self.clausulas if c.severidad in ("alto", "critico")]

    def to_dict(self) -> dict:
        return {
            "contrato_id": self.contrato_id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "fecha_analisis": self.fecha_analisis,
            "total_clausulas": len(self.clausulas),
            "clausulas": [c.evaluar() for c in self.clausulas],
        }


class Dictamen:
    _DESCUENTOS = {"bajo": 5, "medio": 15, "alto": 25, "critico": 40}

    def __init__(self, contrato: Contrato, estadisticas: dict):
        self.contrato = contrato
        self.estadisticas = estadisticas
        self.score = self._calcular_score()
        self.nivel = self._determinar_nivel()

    def _calcular_score(self) -> int:
        score = 100
        for clausula in self.contrato.clausulas:
            score -= self._DESCUENTOS.get(clausula.severidad, 0)
        return max(score, 0)

    def _determinar_nivel(self) -> str:
        if self.score < 40:
            return "CRITICO"
        if self.score < 60:
            return "ALTO"
        if self.score < 80:
            return "MEDIO"
        return "BAJO"

    def _recomendacion_final(self) -> str:
        mensajes = {
            "CRITICO": "🚨 Contrato con riesgos críticos. NO firmar sin revisión legal urgente.",
            "ALTO":    "⚠️ Contrato con riesgos significativos. Se recomienda revisión legal.",
            "MEDIO":   "🔍 Contrato con riesgos moderados. Revisar cláusulas observadas.",
            "BAJO":    "✅ Contrato con bajo nivel de riesgo. Puede proceder con precaución.",
        }
        return mensajes[self.nivel]

    def resumen(self) -> dict:
        return {
            "contrato_id": self.contrato.contrato_id,
            "nombre": self.contrato.nombre,
            "categoria": self.contrato.categoria,
            "fecha_analisis": self.contrato.fecha_analisis,
            "score": self.score,
            "nivel_riesgo": self.nivel,
            "recomendacion_final": self._recomendacion_final(),
            "estadisticas": self.estadisticas,
            "clausulas_riesgosas": len(self.contrato.clausulas_riesgosas()),
            "total_clausulas": len(self.contrato.clausulas),
        }
