from datetime import datetime


class Clausula:
    NIVELES_RIESGO = {"bajo": 1, "medio": 2, "alto": 3, "critico": 4}

    def __init__(self, id: str, tipo: str, texto: str, severidad: str):
        self.id = id
        self.tipo = tipo
        self.texto = texto
        self.severidad = severidad.lower()
        self.es_riesgosa = self.severidad in ("alto", "critico")

    def evaluar(self) -> dict:
        return {
            "id": self.id,
            "tipo": self.tipo,
            "texto": self.texto,
            "severidad": self.severidad,
            "es_riesgosa": self.es_riesgosa,
            "peso_riesgo": self.peso_riesgo(),
        }

    def peso_riesgo(self) -> int:
        return self.NIVELES_RIESGO.get(self.severidad, 1)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id} tipo={self.tipo} severidad={self.severidad}>"


class ClausulaLaboral(Clausula):
    _ARTICULOS = {
        "despido":           "Art. 22° LPCL — causa justa de despido",
        "jornada":           "Art. 25° Constitución — jornada máxima 8h",
        "remuneracion":      "Art. 24° Constitución — remuneración equitativa",
        "cese_colectivo":    "Art. 46° LPCL — cese colectivo por causas objetivas",
        "vacaciones":        "Art. 10° D.Leg. 713 — derecho a vacaciones anuales",
        "horas_extra":       "Art. 9° D.Leg. 854 — trabajo en sobretiempo voluntario",
        "default":           "Art. 4° LPCL — contrato de trabajo",
    }

    def evaluar(self) -> dict:
        base = super().evaluar()
        clave = next((k for k in self._ARTICULOS if k in self.tipo.lower()), "default")
        base.update({
            "categoria": "laboral",
            "articulo_referencia": self._ARTICULOS[clave],
            "recomendacion": (
                "Verificar cumplimiento de la Ley de Productividad y Competitividad Laboral "
                "y la Constitución Política del Perú (Art. 22°-29°)."
            ),
        })
        return base


class ClausulaArrendamiento(Clausula):
    _ARTICULOS = {
        "renta":          "Art. 1666° CC — contrato de arrendamiento",
        "plazo":          "Art. 1688° CC — duración del arrendamiento",
        "conservacion":   "Art. 1681° CC — obligaciones del arrendatario",
        "resolucion":     "Art. 1697° CC — resolución del contrato",
        "subarrendamiento": "Art. 1692° CC — subarrendamiento",
        "default":        "Art. 1666° CC — arrendamiento de bienes",
    }

    def evaluar(self) -> dict:
        base = super().evaluar()
        clave = next((k for k in self._ARTICULOS if k in self.tipo.lower()), "default")
        base.update({
            "categoria": "arrendamiento",
            "articulo_referencia": self._ARTICULOS[clave],
            "recomendacion": (
                "Revisar las obligaciones del arrendador y arrendatario conforme "
                "al Código Civil Peruano (Arts. 1666°-1712°)."
            ),
        })
        return base


class ClausulaServicios(Clausula):
    _ARTICULOS = {
        "honorarios":     "Art. 1764° CC — contrato de locación de servicios",
        "plazo":          "Art. 1768° CC — duración del contrato de servicios",
        "obligaciones":   "Art. 1766° CC — obligaciones del locador",
        "resolucion":     "Art. 1786° CC — resolución por incumplimiento",
        "confidencial":   "Art. 1770° CC — deber de reserva profesional",
        "default":        "Art. 1764° CC — locación de servicios",
    }

    def evaluar(self) -> dict:
        base = super().evaluar()
        clave = next((k for k in self._ARTICULOS if k in self.tipo.lower()), "default")
        base.update({
            "categoria": "servicios",
            "articulo_referencia": self._ARTICULOS[clave],
            "recomendacion": (
                "Verificar la naturaleza civil del vínculo para evitar desnaturalización "
                "laboral conforme al Código Civil (Arts. 1764°-1770°)."
            ),
        })
        return base


class ClausulaCompraventa(Clausula):
    _ARTICULOS = {
        "precio":         "Art. 1529° CC — contrato de compraventa",
        "entrega":        "Art. 1549° CC — obligación de entrega del bien",
        "saneamiento":    "Art. 1484° CC — saneamiento por evicción",
        "garantia":       "Art. 1503° CC — garantía de buen funcionamiento",
        "resolucion":     "Art. 1562° CC — resolución por falta de pago",
        "propiedad":      "Art. 1529° CC — transferencia de propiedad",
        "default":        "Art. 1529° CC — compraventa de bienes",
    }

    def evaluar(self) -> dict:
        base = super().evaluar()
        clave = next((k for k in self._ARTICULOS if k in self.tipo.lower()), "default")
        base.update({
            "categoria": "compraventa",
            "articulo_referencia": self._ARTICULOS[clave],
            "recomendacion": (
                "Confirmar condiciones de transferencia de propiedad y saneamiento "
                "conforme al Código Civil Peruano (Arts. 1529°-1601°)."
            ),
        })
        return base


_FABRICA = {
    "laboral":       ClausulaLaboral,
    "arrendamiento": ClausulaArrendamiento,
    "servicios":     ClausulaServicios,
    "compraventa":   ClausulaCompraventa,
}


def fabricar_clausula(categoria: str, id: str, tipo: str, texto: str, severidad: str) -> Clausula:
    cls = _FABRICA.get(categoria.lower(), Clausula)
    return cls(id=id, tipo=tipo, texto=texto, severidad=severidad)
