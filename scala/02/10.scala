def power(x: Double, n: Int): Double = {
  if (n == 0) {
  	1
  }
  else if (n < 0) {
  	1 / power(x, -n)
  }
  else if (n % 2 == 1) {
  	x * power(x, n - 1)
  }
  else {
  	val y = power(x, n / 2)
  	y * y
  }
}
