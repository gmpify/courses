import scala.collection.JavaConversions.propertiesAsScalaMap
val properties: scala.collection.Map[String, String] = java.lang.System.getProperties

val keys_length = for ((k, v) <- properties) yield k.length

val largest_key_length = keys_length.max

for ((k, v) <- properties) {
	val spaces_to_print = largest_key_length - k.length
	println(f"${k}%s${" " * spaces_to_print}%s | ${v}%s")
}
