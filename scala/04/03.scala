import scala.collection.JavaConversions._
val in : Iterator[String] = new java.util.Scanner(new java.io.File("myfile.txt"))

def process(words : Iterator[String]) = {
	var temp_words = Map[String, Int]().withDefaultValue(0)
	while (words.hasNext()) {
		val word = words.next()
		val current_count = temp_words(word)
		temp_words = temp_words + (word -> (current_count + 1))
	}
	temp_words
}

print(process("test one test two".split(" ").iterator))
