import os.Path

val cd = os.home/"courses"/"scala"/"09"

// 01
val lines01 = os.read.lines(cd/"test01.txt")

if (os.exists(cd/"test01.txt")) os.remove(cd/"test01.txt")
for (line <- lines01.reverse) {
  os.write.append(cd/"test01.txt", line + "\n")
}

// 02
val lines02 = os.read.lines(cd/"test02.txt")

if (os.exists(cd/"test02a.txt")) os.remove(cd/"test02a.txt")

for (line <- lines02) {
  val l = line.replaceAll("\\t", " " * 4)
  os.write.append(cd/"test02a.txt", l + "\n")
}

// 03
for {
  line <- os.read.lines(cd/"test03.txt")
  word <- "\\w{12,}".r.findAllIn(line)
} {
  println(word)
}

os.read.lines(cd/"test03.txt").foreach(line => "\\w{12,}".r.findAllIn(line).foreach(word => println(word)))

// 04
var n = Array.empty[Double]
for (line <- os.read.lines(cd/"test04.txt")) {
  for (number <- line.split(" ")) {
    n = n :+ number.toDouble
  }
}
println("sum", n.sum)
println("avg", n.sum / n.length)
println("max", n.max)
println("min", n.min)

// 05
if (os.exists(cd/"test05.txt")) os.remove(cd/"test05.txt")

for (i <- 0 to 20) {
  val pow = math.pow(2, i).toInt
  val reciprocal = 1.0/pow
  os.write.append(cd/"test05.txt", f"$pow\t$reciprocal\n")
}

// 06
//for (line <- os.read.lines(cd/"test07.txt")) {
//  for (token <- "\".*".r.findAllIn(line)) {
//    println(token)
//  }
//}

// 07
//for (line <- os.read.lines(cd/"test07.txt")) {
//  for (token <- "(\\d+\\.\\d+)".r.findAllIn(line)) {
//    println(token)
//  }
//}

// 08

// 09
var count = 0
val files: IndexedSeq[Path] = os.walk(os.home/"courses")
for (file <- files if file.ext == "class") {
    count += 1
    println(file.toString)
}

println(count)

// 10