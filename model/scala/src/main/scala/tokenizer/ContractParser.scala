package tokenizer

import models.{Contract, Clause}
import utils.TextNormalizer
import ujson.*

object ContractParser:
  def parsear(id: String, nombre: String, texto: String): Contract =
    val textoNorm = TextNormalizer.normalizar(texto)
    val tokens    = Tokenizer.tokenizar(textoNorm)
    val clausulas = ClauseExtractor.extraer(textoNorm, tokens)
    Contract(id, nombre, texto, clausulas)

  def toJson(contrato: Contract): String =
    val json = ujson.Obj(
      "contrato_id" -> contrato.id,
      "nombre"      -> contrato.nombre,
      "clausulas"   -> contrato.clausulas.map { c =>
        ujson.Obj(
          "id"     -> c.id,
          "tipo"   -> c.tipo,
          "texto"  -> c.texto,
          "partes" -> ujson.Arr.from(c.partes)
        )
      }
    )
    ujson.write(json, indent = 2)
