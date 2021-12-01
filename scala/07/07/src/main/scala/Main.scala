object Main extends App {
  import java.util.{HashMap => JavaHashMap}
  import scala.collection.mutable.{HashMap => ScalaHashMap}

  val javaMap = new JavaHashMap[String, Int]() {
    put("abc", 1)
    put("def", 2)
    put("ghi", 3)
  }
  
  val scalaMap = ScalaHashMap[String, Int]()

  javaMap.forEach(scalaMap(_) = _)

  println(javaMap)
  println(scalaMap)
}
