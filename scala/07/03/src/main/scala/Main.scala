object Main extends App {
  val numbers = new random.Numbers
  
  numbers.setSeed(6)

  for( i <- 0.to(4)) {
    println(numbers.nextInt())
    println(numbers.nextDouble())  
  }
}
