import scala.collection.mutable.ListBuffer
// 1

def indexes(input: String) = {
  val output = scala.collection.mutable.Map[Char, Set[Int]]()
  val input_with_index = input.zipWithIndex
  for (c <- input_with_index) output(c._1) = output.getOrElse(c._1, Set()) + c._2
  output
}

indexes("Mississippi")


// 2 ????
//def indexes2(input: String) = {
//  val input_with_index = input.zipWithIndex
//  (scala.collection.immutable.Map[Char, List[Int]]() /: input_with_index) {
//    (m, c) => m + (c -> (m.getOrElse(c._1, List[Int]()) + c._2))
//  }
//}
//
//indexes2("Mississippi")


// 3
def remove1(input: ListBuffer[String]) = {
  for (i <- (input.size to 0) if i % 2 == 0) input.remove(i)
  input
}

def remove2(input: ListBuffer[String]) = {
  input.zipWithIndex.filter(i => i._2 % 2 == 0).map(i => i._1)
}

remove1(ListBuffer("M", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"))

remove2(ListBuffer("M", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"))


// 4
def combine(a: Array[String], m: Map[String, Int]): Array[Int] = {
  a.flatMap(i => m.get(i))
}

combine(Array("Tom", "Fred", "Harry"), Map("Tom" -> 3, "Dick" -> 4, "Harry" -> 5))


// 5 ????


// 6 ????
val lst = List(1, 2, 3, 4, 5)

val test1 = (lst :\ List[Int]())(_ :: _)

val test2 = (List[Int]() /: lst)(_ :+ _)

// 7
val prices = List(5.0, 20.0, 9.95)
val quantities = List(10, 2, 1)
//val output7 = (prices zip quantities) map { (_ * _).tupled }

// 8
