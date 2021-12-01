class Time(hours: Int, minutes: Int) {
	val timeInMinutes = hours * 60 + minutes
	def before(other: Time) : Boolean = {
		timeInMinutes < other.timeInMinutes
	}
}

val midNight = new Time(0, 0)
val midDay = new Time(12, 0)
val halfPastMidDay = new Time(12, 30)

println(midNight.before(midDay))
println(halfPastMidDay.before(midDay))
