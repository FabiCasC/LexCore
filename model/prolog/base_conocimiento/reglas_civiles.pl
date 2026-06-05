clausula_riesgosa(Id, penalidad, critico) :-
    clausula(Id, penalidad, Texto),
    sub_atom(Texto, _, _, _, 'interés compuesto').

clausula_riesgosa(Id, rescision, alto) :-
    clausula(Id, rescision, Texto),
    \+ sub_atom(Texto, _, _, _, 'plazo'),
    \+ sub_atom(Texto, _, _, _, 'notificación').

clausula_valida_civil(Id) :-
    clausula(Id, Tipo, _),
    tipo_clausula(Tipo),
    \+ clausula_riesgosa(Id, _, _).
