import tokenizer.ContractParser

object Main:
  def main(args: Array[String]): Unit =
    val texto    = scala.io.Source.stdin.mkString
    val id       = if args.length > 0 then args(0) else "contrato_001"
    val nombre   = if args.length > 1 then args(1) else "Contrato"
    val contrato = ContractParser.parsear(id, nombre, texto)
    println(ContractParser.toJson(contrato))
