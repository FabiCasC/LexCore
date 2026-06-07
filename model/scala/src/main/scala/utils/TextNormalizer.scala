package utils

object TextNormalizer:
  def normalizar(texto: String): String =
    texto
      .trim
      .replaceAll("\\s+", " ")
      .replaceAll("[\\r\\n]+", "\n")
