clausula_riesgosa(Id, penalidad, alto) :-
    clausula(Id, penalidad, _).

clausula_riesgosa(Id, plazo, medio) :-
    clausula(Id, plazo, Texto),
    \+ sub_atom(Texto, _, _, _, dias),
    \+ sub_atom(Texto, _, _, _, 'días').

clausula_riesgosa(Id, general, bajo) :-
    clausula(Id, general, Texto),
    atom_length(Texto, Len),
    Len < 30.

clausula_incompleta(Id) :-
    clausula(Id, _, Texto),
    atom_length(Texto, Len),
    Len < 15.

contrato_valido :-
    \+ clausula_riesgosa(_, _, critico).
