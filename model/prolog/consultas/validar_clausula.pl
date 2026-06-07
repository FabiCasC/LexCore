validar(Id, riesgo(Tipo, Severidad)) :-
    clausula_riesgosa(Id, Tipo, Severidad), !.
validar(Id, valida) :-
    clausula(Id, _, _).
