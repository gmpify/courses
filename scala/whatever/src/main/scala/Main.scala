object Main extends App {
  val token = "e8651fd83d3197a099d43fd73f9e1d2a02cffd46"
  val auth: requests.RequestAuth = ("gparreiras", token)

  def fetchRepos(username: String): List[String] = {
    val resultText = requests
      .get(s"https://github.bamtech.co/api/v3/users/${username}/repos", auth)
      .data
      .text

    val resultJson = ujson.read(resultText)

    resultJson.arr.map(elem => elem("full_name").str).toList
  }

  println(fetchRepos("gparreiras").mkString("\n"))
  println(fetchRepos("lbria").mkString("\n"))

}
