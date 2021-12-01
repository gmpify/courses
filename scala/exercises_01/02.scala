class MultiMap(val map: Map[_, _]) {
	def add(other: MultiMap) : MultiMap = {
		new MultiMap(map ++ other.map)
	}
	// def remove(other: MultiMap) : MultiMap = {
	// 	val keys = other.map.keys
	// }
	// def get(key: _) : _ = {
	// 	new Multimap(map.get(key))
	// }
}

val a = new MultiMap(Map[String, Double]("foo" -> 99, "bar" -> 2.1, "xpto" -> 100))
val b = new MultiMap(Map[String, Double]("abc" -> 9, "def" -> 212))

val add = a.add(b)
print(add.map)
// val remove = add.remove(b)
// print(remove.map)
