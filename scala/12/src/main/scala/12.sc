// 01

def values(fun: (Int) => Int, low: Int, high: Int) = {
  for (i <- low.to(high)) yield (i, fun(i))
}

values(x => x * x, -5, 5)

// 02
def largest(array: Array[Int]): Int = {
  array.reduceLeft(_.max(_))
}

val a02 = Array(1, 5, 10, 20, -2, 3)
largest(a02)

// 03
def factorial(n: Int): Int = {
  if (n < 1) {
    1
  }
  else {
    1.to(n).reduceLeft(_ * _)
  }
}

factorial(0)
factorial(3)
factorial(4)
factorial(5)

// 04
def factorial04(n: Int): Int = {
  1.to(n).foldLeft(1)(_ * _)
}

factorial(0)
factorial(3)
factorial(4)
factorial(5)

// 05
def largest05(fun: (Int) => Int, inputs: Seq[Int]): Int = {
  inputs.map(fun).max
}

largest05(x => 10 * x - x * x, 1 to 10)

// 06
def largestAt(fun: (Int) => Int, inputs: Seq[Int]): Int = {
  inputs
    .map(x => (x, fun(x)))
    .maxBy(t => t._2)
    ._1
}

largestAt(x => 10 * x - x * x, 1 to 10)

// 07
val pairs = (1 to 10) zip (11 to 20)

def adjustToPair(fun: (Int, Int) => Int) = {
  (x: (Int, Int)) => fun(x._1, x._2)
}

adjustToPair(_ * _)((6, 7))

pairs.map(adjustToPair(_ + _))

// 08
val a = Array("Hello", "World")
val b = Array(5, 5)
a.corresponds(b)(_.length.equals(_))

// 09

// 10
