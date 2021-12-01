/////////////////
// EXERCISE 01 //
/////////////////
class BankAccount(initialBalance: Double) {
  private var balance = initialBalance
  def currentBalance = balance
  def deposit(amount: Double) = { balance += amount; balance }
  def withdraw(amount: Double) = { balance -= amount; balance }
}

class CheckingAccount(initialBalance: Double) extends BankAccount(initialBalance) {
  val operationFee: Int = 1

  override def deposit(amount: Double) = {
    super.deposit(amount - operationFee)
  }

  override def withdraw(amount: Double) = {
    super.withdraw(amount + operationFee)
  }
}

val a1 = new CheckingAccount(1000)
println(a1.currentBalance)
a1.deposit(100)
println(a1.currentBalance)
a1.withdraw(100)
println(a1.currentBalance)


/////////////////
// EXERCISE 02 //
/////////////////
class SavingsAccount(initialBalance: Double) extends BankAccount(initialBalance) {
  private val operationFee: Int = 1
  private val freeOperations: Int = 3
  private val interestRate:Double = 0.05

  private var availableOperations:Int = freeOperations

  override def deposit(amount: Double) = {

    val netAmount: Double = if (availableOperations > 0) {
      availableOperations -= 1
      amount
    }
    else {
      amount - operationFee
    }
    super.deposit(netAmount)
  }

  override def withdraw(amount: Double) = {

    val netAmount: Double = if (availableOperations > 0) {
      availableOperations -= 1
      amount
    }
    else {
      amount + operationFee
    }
    super.withdraw(netAmount)
  }

  def earnMonthlyInterest(): Unit = {
    super.deposit(super.currentBalance * interestRate)
    availableOperations = freeOperations
  }
}

val a2 = new SavingsAccount(1000)
println(a2.currentBalance)
a2.deposit(100)
a2.deposit(100)
a2.deposit(100)
println(a2.currentBalance)
a2.withdraw(100)
println(a2.currentBalance)
a2.earnMonthlyInterest()
println(a2.currentBalance)


/////////////////
// EXERCISE 04 //
/////////////////

abstract class Item {
  def price: Double
  def description: String
}

class SimpleItem(val price: Double, val description: String) extends Item

class Bundle extends Item {
  var items = Array.empty[Item]

  def price: Double = {
    items.map(_.price).sum
  }

  def description: String = {
    val itemsDescription = items.map(_.description).mkString(", ")
    "Bundle of the following items: " + itemsDescription
  }

  def add(item: Item): Unit = {
    items = items :+ item
  }
}

val a4 = new SimpleItem(10, "toy")
a4.description
a4.price

val b4 = new Bundle
b4.add(a4)
b4.price
b4.description

b4.add(a4)
b4.price
b4.description


/////////////////
// EXERCISE 05 //
/////////////////

class Point(val x: Double, val y: Double)

class LabeledPoint(val label: String, x: Double, y: Double) extends Point(x, y)

val a5 = new LabeledPoint("Black Thursday", 1929, 230.07)
a5.x
a5.y
a5.label


/////////////////
// EXERCISE 06 //
/////////////////

abstract class Shape {
  def centerPoint: Point
}

class Rectangle(bottomLeft: Point, topRight: Point) extends Shape {
  def centerPoint: Point = {
    val x = bottomLeft.x + (topRight.x - bottomLeft.x) / 2
    val y = bottomLeft.y + (topRight.y - bottomLeft.y) / 2
    new Point(x, y)
  }
}

class Circle(val centerPoint: Point, radius: Int) extends Shape

val a6 = new Rectangle(new Point(0,0), new Point(2, 4))
val b6 = a6.centerPoint
b6.x
b6.y


/////////////////
// EXERCISE 07 //
/////////////////

class Square(x: Int, y: Int, width: Int, height: Int) extends java.awt.Rectangle(x, y, width, height) {
  def this(x: Int, y: Int, width: Int) = {
    this(x, y, width, width)
  }

  def this(width: Int) = {
    this(0, 0, width, width)
  }

  def this() = {
    this(0, 0, 0, 0)
  }
}

val a7 = new Square()
val b7 = new Square(2)
val c7 = new Square(2, 2, 2)

/////////////////
// EXERCISE 09 //
/////////////////