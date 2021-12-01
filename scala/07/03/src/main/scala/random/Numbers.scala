package random

class Numbers {
  import math.pow
  private val a: Long = 1664525
  private val b: Long = 1013904223
  private val n: Int = 32
  private var previous: Long = 0

  def setSeed(seed: Int): Unit = {
    previous = seed
  }
  
  def nextInt(): Int = {
    val current = (previous * a + b) % pow(2, n) % Int.MaxValue
    previous = current.toLong
    current.toInt
  }

  def nextDouble(): Double = {
    val current = (previous * a + b) % pow(2, n)
    previous = current.toLong
    current
  }
}
