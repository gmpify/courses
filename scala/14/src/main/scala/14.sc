// 02
def swap2(input: (Int, Int)): (Int, Int) = {
  input match {
    case (x, y) => (y, x)
  }
}

val a02 = (2, 3)
println(swap2(a02))



// 03
def swap3(input: Array[Int]): Array[Int] = {
  input match {
    case Array(x, y, rest @ _*) => Array(y, x) ++ rest
    case _ => input
  }
}

val a03 = Array(1, 2, 3, 4)
println(swap3(a03).mkString(" "))
val b03 = Array(1)
println(swap3(b03).mkString(" "))
val c03 = Array(10, 20)
println(swap3(c03).mkString(" "))



// 04
abstract class Item
case class Article(description: String, price: Double) extends Item
case class Bundle(description: String, discount: Double, items: Item*) extends Item
case class Multiple(quantity: Int, item: Item) extends Item

def price(it: Item): Double = it match {
  case Article(_, p) => p
  case Bundle(_, disc, its @ _*) => its.map(price _).sum - disc
  case Multiple(q, i: Item) => q * price(i)
}

val t = Multiple(10, Article("Blackwell Toaster", 29.95))
println(price(t))



// 05 ?????????????
//def leafSum(input: List[Any], sum: Int = 0): Int = {
//  elem match {
//    case i: Int => sum + i
//    case l: List[Any] => sum + leafSum(l, sum)
//  }
//}

//val test = List(List(3, 8), 2, List(5))
//println(leafSum(test))



// 06
sealed abstract class BinaryTree
case class Leaf(value: Int) extends BinaryTree
case class Node(left: BinaryTree, right: BinaryTree) extends BinaryTree

def leafSum06(input: BinaryTree): Int = input match {
  case Node(l, r) => leafSum06(l) + leafSum06(r)
  case Leaf(v) => v
}

val bt06 = Node(Node(Leaf(1), Leaf(2)), Node(Leaf(3),Leaf(4)))
println(leafSum06(bt06))



// 07
sealed abstract class Tree07
case class Leaf07(value: Int) extends Tree07
case class Node07(nodes: Tree07*) extends Tree07

def leafSum07(input: Tree07): Int = input match {
  case Node07(n1 @ _*) => n1.map(leafSum07).sum
  case Leaf07(v) => v
}

val bt07 = Node07(Node07(Leaf07(3), Leaf07(8)), Node07(), Leaf07(2), Node07(Leaf07(5)))
println(leafSum07(bt07))



// 08
sealed abstract class Tree08
case class Leaf08(value: Int) extends Tree08
case class Node08(operator: String, nodes: Tree08*) extends Tree08

def leafSum08(input: Tree08): Int = input match {
  case Node08("+", n1 @ _*) => n1.map(leafSum08 _).sum
  case Node08("-", n1 @ _*) => n1.map(leafSum08 _).sum * (-1)
  case Node08("*", n1 @ _*) => n1.map(leafSum08 _).product
  case Leaf08(v) => v
  case _ => throw new Exception("Operator not available")
}

val bt08 = Node08("+",
  Node08("*",
    Leaf08(3),
    Leaf08(8)
  ),
  Leaf08(2),
  Node08("-",
    Leaf08(5),
    Leaf08(8),
    Leaf08(8)
  )
)
println(leafSum08(bt08))

// 09 ???????
// 10 ???????
import math.sqrt

def f(x: Double) = if (x != 1) Some(1 / (x - 1)) else None
def g(x: Double) = if (x >= 0) Some(sqrt(x)) else None
//val h = compose(g, f) // h(x) should be g(f(x))

type DD = Double => Option[Double]

def compose(a: DD, b: DD): DD = { (d: Double) =>
  a(d) match {
    case Some(d2) => b(d2)
    case None => None
  }
}

val h = compose(f, g)

h(0)
h(1)
h(2)
h(65)
h(1.25)
f(1.25)