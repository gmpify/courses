val originalPrices = Map[String, Double]("foo" -> 99, "bar" -> 2.1, "xpto" -> 100)

val newPrices = for ((key, value) <- originalPrices) yield (key, 0.9 * value)
