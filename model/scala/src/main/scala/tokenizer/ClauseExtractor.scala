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
      Clause(idx + 1, detectarTipo(seg), seg.trim, List.empty)
    }

  private def detectarTipo(texto: String): String =
    val lower = texto.toLowerCase
    tiposClausula
      .find { case (_, palabras) => palabras.exists(lower.contains) }
      .map(_._1)
      .getOrElse("general")
