verificar_contrato(aprobado) :-
    contrato_valido, !.
verificar_contrato(con_riesgos).

resumen_contrato(Total, Riesgosos) :-
    aggregate_all(count, clausula(_, _, _), Total),
    aggregate_all(count, clausula_riesgosa(_, _, _), Riesgosos).
