import scala.collection.mutable.ArrayBuffer

val a = ArrayBuffer[Int](1, 5, -2, 0, 3, -9, -8, 2)

val positionsWithNegatives = for (i <- a.indices if a(i) < 0) yield i

val positionsToRemove = positionsWithNegatives.tail

for (i <- positionsToRemove.reverse) {
	a.remove(i)
}

a
