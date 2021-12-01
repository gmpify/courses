class Time(val hours: Int, val minutes: Int) {
	def before(other: Time) : Boolean = {
		((hours < other.hours) || (hours == other.hours && minutes < other.minutes))
	}
}

val midNight = new Time(0, 0)
val midDay = new Time(12, 0)
val halfPastMidDay = new Time(12, 30)

println(midNight.before(midDay))
println(halfPastMidDay.before(midDay))
