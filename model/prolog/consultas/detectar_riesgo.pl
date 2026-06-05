riesgos_contrato(Hallazgos) :-
    findall(
        hallazgo(Id, Tipo, Severidad),
        clausula_riesgosa(Id, Tipo, Severidad),
        Hallazgos
    ).

nivel_critico :-
    clausula_riesgosa(_, _, critico).
