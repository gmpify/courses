def product(input: String): Long = {
  if (input == "") {
    1
  }
  else {
    input.head.toLong * product(input.tail)
  }
}
