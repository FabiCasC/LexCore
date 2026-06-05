clausula_riesgosa(Id, confidencialidad, alto) :-
    clausula(Id, confidencialidad, Texto),
    \+ sub_atom(Texto, _, _, _, 'plazo de vigencia').

clausula_riesgosa(Id, penalidad, medio) :-
    clausula(Id, penalidad, Texto),
    sub_atom(Texto, _, _, _, 'exclusividad absoluta').

clausula_valida_comercial(Id) :-
    clausula(Id, Tipo, _),
    tipo_clausula(Tipo),
    \+ clausula_riesgosa(Id, _, _).
