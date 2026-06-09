:- set_prolog_flag(encoding, utf8).
:- multifile clausula_riesgosa/3.

clausula_riesgosa(Id, penalidad, alto) :-
    clausula(Id, penalidad, _).

clausula_riesgosa(Id, penalidad, critico) :-
    clausula(Id, penalidad, Texto),
    (   sub_atom(Texto, _, _, _, 'interes compuesto')
    ;   sub_atom(Texto, _, _, _, 'interes acumulado')
    ).

clausula_riesgosa(Id, penalidad, critico) :-
    clausula(Id, penalidad, Texto),
    (   sub_atom(Texto, _, _, _, '50%')
    ;   sub_atom(Texto, _, _, _, '60%')
    ;   sub_atom(Texto, _, _, _, '70%')
    ;   sub_atom(Texto, _, _, _, '80%')
    ;   sub_atom(Texto, _, _, _, '90%')
    ;   sub_atom(Texto, _, _, _, '100%')
    ).


clausula_riesgosa(Id, plazo, medio) :-
    clausula(Id, plazo, Texto),
    \+ sub_atom(Texto, _, _, _, dias),
    \+ sub_atom(Texto, _, _, _, meses),
    \+ sub_atom(Texto, _, _, _, semanas),
    \+ sub_atom(Texto, _, _, _, anios),
    \+ sub_atom(Texto, _, _, _, 'años').

clausula_riesgosa(Id, rescision, alto) :-
    clausula(Id, rescision, Texto),
    \+ sub_atom(Texto, _, _, _, preaviso),
    \+ sub_atom(Texto, _, _, _, notificacion),
    \+ sub_atom(Texto, _, _, _, 'aviso previo').

clausula_riesgosa(Id, general, bajo) :-
    clausula(Id, general, Texto),
    atom_length(Texto, Len),
    Len < 30.

clausula_riesgosa(Id, general, critico) :-
    clausula(Id, _, Texto),
    (   sub_atom(Texto, _, _, _, 'no sera responsable')
    ;   sub_atom(Texto, _, _, _, 'exime de responsabilidad')
    ;   sub_atom(Texto, _, _, _, 'exonera de responsabilidad')
    ;   sub_atom(Texto, _, _, _, 'sin responsabilidad alguna')
    ;   sub_atom(Texto, _, _, _, 'renuncia a reclamar')
    ).

clausula_riesgosa(Id, general, alto) :-
    clausula(Id, _, Texto),
    (   sub_atom(Texto, _, _, _, 'a sola decision')
    ;   sub_atom(Texto, _, _, _, 'a su sola discrecion')
    ;   sub_atom(Texto, _, _, _, 'unilateralmente')
    ;   sub_atom(Texto, _, _, _, 'sin necesidad de causa')
    ).

clausula_incompleta(Id) :-
    clausula(Id, _, Texto),
    atom_length(Texto, Len),
    Len < 15.

contrato_valido :-
    \+ clausula_riesgosa(_, _, critico).
