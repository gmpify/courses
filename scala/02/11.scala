import java.time._

implicit class DateInterpolator(val sc: StringContext) extends AnyVal {
  def date(args: Any*): LocalDate = {
    if (args.size != 3) throw new IllegalArgumentException("Only 3 arguments accepted")
    if (sc.parts(1) != "-" || sc.parts(2) != "-") throw new IllegalArgumentException("Arguments must be separated by dashes")
    for (arg <- args) if (!arg.isInstanceOf[Int]) throw new IllegalArgumentException("Arguments must be integers")

    val year = args(0).toString.toInt
    val month = args(1).toString.toInt
    val day = args(2).toString.toInt

    LocalDate.of(year, month, day)
  }
}
