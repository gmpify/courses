val days = scala.collection.mutable.LinkedHashMap(
	"Monday" -> java.util.Calendar.MONDAY,
	"Tuesday" -> java.util.Calendar.TUESDAY,
	"Wednesday" -> java.util.Calendar.WEDNESDAY,
	"Thursday" -> java.util.Calendar.THURSDAY,
	"Friday" -> java.util.Calendar.FRIDAY,
	"Saturday" -> java.util.Calendar.SATURDAY,
	"Sunday" -> java.util.Calendar.SUNDAY
)

for (day <- days) print (day)

val daysOtherOrder = scala.collection.mutable.LinkedHashMap(
	"Friday" -> java.util.Calendar.FRIDAY,
	"Monday" -> java.util.Calendar.MONDAY,
	"Thursday" -> java.util.Calendar.THURSDAY,
	"Tuesday" -> java.util.Calendar.TUESDAY,
	"Wednesday" -> java.util.Calendar.WEDNESDAY,
	"Sunday" -> java.util.Calendar.SUNDAY,
	"Saturday" -> java.util.Calendar.SATURDAY
)

for (day <- daysOtherOrder) print (day)
