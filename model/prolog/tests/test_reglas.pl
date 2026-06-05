:- begin_tests(reglas_lexcore).

test(clausula_penalidad_es_riesgosa) :-
    assertz(clausula(99, penalidad, 'Se aplicará multa por incumplimiento')),
    clausula_riesgosa(99, penalidad, alto),
    retract(clausula(99, penalidad, _)).

test(clausula_general_corta_es_riesgosa) :-
    assertz(clausula(98, general, 'Ver anexo')),
    clausula_riesgosa(98, general, bajo),
    retract(clausula(98, general, _)).

test(contrato_sin_clausulas_es_valido) :-
    contrato_valido.

:- end_tests(reglas_lexcore).
