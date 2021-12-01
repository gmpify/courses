import java.lang.System._

object Main extends App {
  val userName:String = getProperty("user.name")
  var password:String = ""
  
  for (c <- "Enter your password: ") {
      out.write(c.toChar)
    }
    out.flush()
  
  var passwordChar:Int = in.read()
  while (passwordChar != 10) { // 10 == \n
    password += passwordChar.toChar
    passwordChar = in.read()
  }

  if (password != "secret") {
    for (c <- f"ERROR Failed login attempt by ${userName}%s\n") {
      err.write(c.toChar)
    }
    err.flush()
  }
  else {
    for (c <- f"Welcome aboard, ${userName}%s!\n") {
      out.write(c.toChar)
    }
    out.flush()
  }
}
