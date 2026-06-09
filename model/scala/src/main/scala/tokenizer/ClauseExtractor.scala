package tokenizer

import models.{Clause, Token}

object ClauseExtractor:
  private val tiposClausula = Map(
    "obligacion"       -> List("debe", "obligado", "responsable", "cumplir"),
    "plazo"            -> List("días", "dias", "meses", "año", "fecha", "plazo", "vencimiento"),
    "penalidad"        -> List("multa", "penalidad", "sanción", "sancion", "incumplimiento"),
    "confidencialidad" -> List("confidencial", "secreto", "privado", "divulgar"),
    "rescision"        -> List("rescindir", "terminar", "finalizar", "disolver")
  )

  def extraer(texto: String, tokens: List[Token]): List[Clause] =
    val patron  = "(?i)(cláusula|clausula|artículo|articulo|sección|seccion)\\s+\\w+\\.?"
    val partes  = texto.split(patron).toList.filter(_.trim.nonEmpty)
    partes.zipWithIndex.map { case (seg, idx) =>
      val textoClausula = seg.trim
      val tipo         = detectarTipo(textoClausula)
      val subpartes    = extraerPartes(textoClausula)
      val puntaje      = calcularPuntaje(textoClausula, tipo)
      Clause(idx + 1, tipo, textoClausula, subpartes, puntaje)
    }

  private def extraerPartes(texto: String): List[String] =
    texto
      .split("[,:;\\n]+")
      .toList
      .map(_.trim)
      .filter(_.nonEmpty)

  private def detectarTipo(texto: String): String =
    val lower = texto.toLowerCase
    tiposClausula
      .find { case (_, palabras) => palabras.exists(lower.contains) }
      .map(_._1)
      .getOrElse("general")

  private def calcularPuntaje(texto: String, tipo: String): Int =
    val palabras = texto
      .split("\\W+")
      .toList
      .map(_.toLowerCase)
      .filter(_.nonEmpty)

    val palabrasClave = tiposClausula.values.toList.flatMap(identity)
    val coincidenciasTipo = tiposClausula
      .getOrElse(tipo, List.empty)
      .count(palabras.contains)

    val coincidenciasGenerales = palabras.count(palabrasClave.contains)
    val longitud = palabras.length

    val base = coincidenciasTipo * 2 + coincidenciasGenerales
    val escala = if longitud > 0 then math.min(10, base + longitud / 20) else 0
    math.max(0, escala)
