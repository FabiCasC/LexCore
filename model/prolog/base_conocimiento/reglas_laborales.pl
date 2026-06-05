clausula_riesgosa(Id, obligacion, critico) :-
    clausula(Id, obligacion, Texto),
    sub_atom(Texto, _, _, _, 'horas extras sin pago').

clausula_riesgosa(Id, plazo, alto) :-
    clausula(Id, plazo, Texto),
    sub_atom(Texto, _, _, _, 'indefinido'),
    \+ sub_atom(Texto, _, _, _, 'preaviso').

clausula_valida_laboral(Id) :-
    clausula(Id, Tipo, _),
    tipo_clausula(Tipo),
    \+ clausula_riesgosa(Id, _, _).
