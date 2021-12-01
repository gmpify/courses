def lteqgt(values: Array[Int], v: Int) = {
	val lt = values.count(_ < v)
	val equal = values.count(_ == v)
	val gt = values.count(_ > v)
	(lt, equal, gt)
}

val testArray = Array(1, 5, 8, 40, -200 , 2, 100, 500, 0)

lteqgt(testArray, 10)
