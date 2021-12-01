class Person(private var privateAge: Int) {
	if (privateAge < 0) privateAge = 0
	def age = privateAge
	def age_=(newValue: Int) {
		if (newValue > privateAge) privateAge = newValue; // Can’t get younger
	}
}

val p = new Person(-10)

println(p.age)
