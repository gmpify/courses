val a = Array(1, -2, 3, 0, -5)

val b = new Array[Int](5)

var last_pos = 0

for (i <- a.indices) {
	if (a(i) > 0) {
		b(last_pos) = a(i)
		last_pos += 1
	}
}

for (i <- a.indices) {
	if (a(i) <= 0) {
		b(last_pos) = a(i)
		last_pos += 1
	}
}
