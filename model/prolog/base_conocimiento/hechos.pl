% Predicado dinámico: clausula(Id, Tipo, Texto)
:- dynamic clausula/3.

tipo_clausula(obligacion).
tipo_clausula(plazo).
tipo_clausula(penalidad).
tipo_clausula(confidencialidad).
tipo_clausula(rescision).
tipo_clausula(general).

nivel_riesgo(bajo,    1).
nivel_riesgo(medio,   2).
nivel_riesgo(alto,    3).
nivel_riesgo(critico, 4).
