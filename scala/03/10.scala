val americaTZs = java.util.TimeZone.getAvailableIDs.filter(_.startsWith("America"))

val americaTZCities = americaTZs.map(_.drop(8))

americaTZCities.sorted
