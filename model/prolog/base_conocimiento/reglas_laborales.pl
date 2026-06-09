:- set_prolog_flag(encoding, utf8).
:- multifile clausula_riesgosa/3.

% REGLA L-1: Horas extras sin pago = CRITICO
% Art. 1354 CC, Art. 1398 CC
clausula_riesgosa(Id, obligacion, critico) :-
    clausula(Id, obligacion, Texto),
    (   sub_atom(Texto, _, _, _, 'horas extras sin pago')
    ;   sub_atom(Texto, _, _, _, 'horas adicionales sin remuneracion')
    ;   sub_atom(Texto, _, _, _, 'trabajo no remunerado')
    ;   sub_atom(Texto, _, _, _, 'sin compensacion adicional')
    ).

% REGLA L-2: Contrato indefinido sin preaviso = ALTO
% Art. 1374 CC
clausula_riesgosa(Id, plazo, alto) :-
    clausula(Id, plazo, Texto),
    sub_atom(Texto, _, _, _, 'indefinid'),
    \+ sub_atom(Texto, _, _, _, preaviso),
    \+ sub_atom(Texto, _, _, _, 'aviso previo').

% REGLA L-3: Penalidad por renuncia del trabajador = CRITICO
% Art. 1354-1355 CC - el derecho a renunciar es irrenunciable
clausula_riesgosa(Id, penalidad, critico) :-
    clausula(Id, penalidad, Texto),
    (   sub_atom(Texto, _, _, _, 'renuncia del trabajador')
    ;   sub_atom(Texto, _, _, _, 'si el trabajador renuncia')
    ;   sub_atom(Texto, _, _, _, 'abandono del cargo')
    ).

% REGLA L-4: No competencia sin limite temporal ni geografico = ALTO
% Art. 1354 CC, Art. 1362 CC
clausula_riesgosa(Id, obligacion, alto) :-
    clausula(Id, obligacion, Texto),
    (   sub_atom(Texto, _, _, _, 'no competencia')
    ;   sub_atom(Texto, _, _, _, 'no podra trabajar')
    ;   sub_atom(Texto, _, _, _, 'no ejercera actividades similares')
    ),
    \+ sub_atom(Texto, _, _, _, anios),
    \+ sub_atom(Texto, _, _, _, meses),
    \+ sub_atom(Texto, _, _, _, 'zona geografica').

% REGLA L-5: Renuncia a beneficios laborales = CRITICO
% Art. 1354-1355 CC - beneficios laborales son irrenunciables
clausula_riesgosa(Id, obligacion, critico) :-
    clausula(Id, obligacion, Texto),
    (   sub_atom(Texto, _, _, _, 'renuncia a CTS')
    ;   sub_atom(Texto, _, _, _, 'sin gratificacion')
    ;   sub_atom(Texto, _, _, _, 'sin beneficios laborales')
    ;   sub_atom(Texto, _, _, _, 'renuncia a vacaciones')
    ).

% REGLA L-6: Exclusividad sin compensacion = MEDIO
% Art. 1397 CC, Art. 1400 CC
clausula_riesgosa(Id, obligacion, medio) :-
    clausula(Id, obligacion, Texto),
    sub_atom(Texto, _, _, _, exclusividad),
    \+ sub_atom(Texto, _, _, _, compensacion),
    \+ sub_atom(Texto, _, _, _, 'remuneracion adicional').

clausula_valida_laboral(Id) :-
    clausula(Id, Tipo, _),
    tipo_clausula(Tipo),
    \+ clausula_riesgosa(Id, _, _).
