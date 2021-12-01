val in = new java.util.Scanner(new java.io.File("myfile.txt"))

var words = scala.collection.mutable.SortedMap[String, Int]().withDefaultValue(0)

while (in.hasNext()) {
	val word = in.next()
	val current_count = words(word)
	words = words + (word -> (current_count + 1))
}

print(words)
