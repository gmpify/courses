val a = Array(1, 2, 3, 4, 5, 6)

for(i <- a.indices if i % 2 == 1) {
	val temp = a(i)
	a(i) = a(i - 1)
	a(i - 1) = temp
}
