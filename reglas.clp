(defrule diagnostico1
  (saciedad S)
(dolor_abdominal S)
(nauseas S)

( vomito S)
( dolor_pecho S)
( fatiga S)
( flatulencia S)
  =>
(assert (diagnostico Indigestion))
  (printout t "Usted tiene: Indigestion" crlf)
)

(defrule diagnostico2
  ( fiebre_alta S)
( dolor_cabeza S)
( dolor_garganta S)
( tos_seca S)
( dolor_muscular S)
( escalofrios S)
( sudoracion S)
( cansancio S)
( debilidad S)
  =>
(assert (diagnostico Gripe ))
  (printout t "Usted tiene: Gripe" crlf)
)

(defrule diagnostico3
  ( dolor_garganta S)
( congestion_nasal S)
( estornudos S)
( tos S)
( dolor_cabeza S)
( dolor_articulacion S)
( fatiga S)

  =>
(assert (diagnostico Resfriado_comun))
  (printout t "Usted tiene: Resfriado común))" crlf)
)

(defrule diagnostico4
  ( estornudos S)
( picazon_nariz S)
( picazon_ojos S)
( picazon_paladar S)
( congestion_nasal S)
( piel_roja S)
( escalofrios S)

  =>
(assert (diagnostico Alergia))
  (printout t "Usted tiene: Alergia ))" crlf)
)


(defrule diagnostico5
  ( piel_roja S)
( picazon S)

  =>
(assert (diagnostico Impetigo))
  (printout t "Usted tiene: Impétigo))" crlf)
)

(defrule diagnostico6
  ( dolor_pecho S)
( tos_flema S)
( fiebre S)
( transpiracion S)
( escalofrios S)

  =>
(assert (diagnostico Neumonia))
  (printout t "Usted tiene: Neumonía))" crlf)
)

(defrule diagnostico7
  ( tos S)
( fiebre_leve S)
( escalofrios  S)

  =>
(assert (diagnostico Bronquitis_aguda))
  (printout t "Usted tiene: Bronquitis aguda))" crlf)
)

(defrule diagnostico8
 ( tos_frecuente S)
( sibilancias S)
( falta_aliento S)
( presion_pecho S)

  =>
(assert (diagnostico Bronquitis_cronica))
  (printout t "Usted tiene: Bronquitis cronica))" crlf)
)

(defrule diagnostico9
 ( falta_aire S)
( presion_pecho S)
( sibilancias S)
( tos S)

  =>
(assert (diagnostico Asma))
  (printout t "Usted tiene: Asma))" crlf)
)

(defrule diagnostico10
 ( dolor_garganta S)
( amigdalas_hinchadas S)
  =>
(assert (diagnostico Infeccion_garganta))
  (printout t "Usted tiene: Infección en la garganta))" crlf)
)

(defrule diagnostico11
 ( diarrea S)
( calambre S)
( fiebre S)
( debilidad S)
  =>
(assert (diagnostico Infeccion_sistema_digestivo))
  (printout t "Usted tiene: Infección del sistema digestivo))" crlf)
)

(defrule diagnostico12
 ( colico_vesicular S)
( dolor_higado S)
  =>
(assert (diagnostico Vesícula_biliar))
  (printout t "Usted tiene: Vesícula biliar))" crlf)
)

(defrule diagnostico13
( dolor_esternon S)
  =>
(assert (diagnostico Apendicitis))
  (printout t "Usted tiene: Apendicitis))" crlf)
)

(defrule diagnostico14
( dolor_pelvis S)
( dificultad_orinar S)
( dolor_orinar S)
  =>
(assert (diagnostico Infeccion_vías_urinarias))
  (printout t "Usted tiene: Infección de vías urinarias))" crlf)
)


(defrule identifica
	
  =>
  (printout t crlf crlf)
  (printout t "Tiene saciedad?: ")
  (bind ?respuesta1(read))
  (printout t crlf crlf)
  (printout t "Tiene dolor_abdominal?: ")
  (bind ?respuesta2(read))
  (printout t crlf crlf)
  (printout t "nauseas: ")
  (bind ?respuesta3(read))

	(printout t crlf crlf)
  (printout t "vomito: ")
  (bind ?respuesta4(read))
(printout t crlf crlf)
  (printout t "Dolor en el pecho: ")
  (bind ?respuesta5(read))
(printout t crlf crlf)
  (printout t "fatiga: ")
  (bind ?respuesta6(read))
(printout t crlf crlf)
  (printout t "flatulencia: ")
  (bind ?respuesta7(read))


(printout t crlf crlf)
  (printout t "Fiebre alta: ")
  (bind ?respuesta8(read))
(printout t crlf crlf)
  (printout t "dolor de cabeza: ")
  (bind ?respuesta9(read))
(printout t crlf crlf)
  (printout t "dolor de garganta: ")
  (bind ?respuesta10(read))
(printout t crlf crlf)
  (printout t "tos seca: ")
  (bind ?respuesta11(read))
(printout t crlf crlf)
  (printout t "dolor muscular: ")
  (bind ?respuesta12(read))
(printout t crlf crlf)
  (printout t "escalofríos: ")
  (bind ?respuesta13(read))
(printout t crlf crlf)
  (printout t "sudoración: ")
  (bind ?respuesta14(read))
(printout t crlf crlf)
  (printout t "cansancio: ")
  (bind ?respuesta15(read))
(printout t crlf crlf)
  (printout t "debilidad: ")
  (bind ?respuesta16(read))

(assert (saciedad ?respuesta1))
(assert (dolor_abdominal ?respuesta2))
(assert (nauseas ?respuesta3))

(assert ( vomito ?respuesta4))
(assert ( dolor_pecho ?respuesta5))
(assert ( fatiga ?respuesta6))
(assert ( flatulencia ?respuesta7))

(assert ( fienre_alta ?respuesta8))
(assert ( dolor_cabeza ?respuesta9))
(assert ( dolor_garganta ?respuesta10))
(assert ( tos_seca ?respuesta11))
(assert ( dolor_muscular ?respuesta12))
(assert ( escalofrios ?respuesta13))
(assert ( sudoracion ?respuesta14))
(assert ( cansancio ?respuesta15))
(assert ( debilidad ?respuesta16))


)