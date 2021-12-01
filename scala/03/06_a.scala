val a = Array[String]("a", "aaaa", "aa")

a.sortWith((a, b) => a.length < b.length)
