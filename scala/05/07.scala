class Person(name: String) {
	if ("""^\w* \w*$""".r.findAllIn(name).toList.length == 0)
		throw new IllegalArgumentException("Constructor only accepts a string containing a first name, a space, and a last name")

	val firstName = name.split(" ").head
	val lastName = name.split(" ").last
}

val p = new Person("Gabriel Parreiras")

println(p.firstName)
println(p.lastName)

val pp = new Person("Gabriel Morais Parreiras")
