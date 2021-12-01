val in = new java.util.Scanner(new java.io.File("myfile.txt"))

val words = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)

while (in.hasNext()) {
	words(in.next()) += 1
}

print(words)
