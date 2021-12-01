import scala.io.Source
import scala.math._

// 01
def readBigInt(file: Source):BigInt =  {
	BigInt(file.mkString.trim)
}

// 02
// TODO Write a function that uses logarithm
def getBigIntDigits1(input: BigInt): Array[Int] = {
	input.toString.toArray.map(_.asDigit)
}

// 03
def concat(input: Array[Int]): BigInt = {
	if (input.filter(_ > 9).size > 0) throw new IllegalArgumentException("There is a digit bigger than 9")

	input.reverse.zipWithIndex.map(t => BigDecimal(t._1 * pow(10, t._2)).toBigInt).sum
}

// 04
def multiplyAdjacents(input: Array[Int], n: Int): Array[Int] = {
	input.sliding(n).map(_.product).toArray
}

// 05
def findAdjacentsWithBiggerProduct(input: BigInt): Array[Int] = {
	val digits = getBigIntDigits1(input)
	
	val digitsProduct = multiplyAdjacents(digits, 4)

	val indexOfBiggerProduct = digitsProduct.indexOf(digitsProduct.max)

	digits.slice(indexOfBiggerProduct, indexOfBiggerProduct + 4)
}

// 06
def findMostRepetition(input: BigInt): Int = {
	val digits = getBigIntDigits1(input)

	val digitsCount = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)

	for (i <- digits) {
		digitsCount(i) += 1
	}

	digitsCount.maxBy(t => t._2)._1
}


val bigIntNumber = readBigInt(Source.fromFile("01.txt"))

findAdjacentsWithBiggerProduct(bigIntNumber)

findMostRepetition(bigIntNumber)

