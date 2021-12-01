class BankAccount {
	private var balance: BigDecimal = 0
	def deposit(ammount: BigDecimal) = { balance += ammount }
	def withdraw(ammount: BigDecimal) = { balance -= ammount }
	def current = balance
}

val account = new BankAccount

println(account.current)

account.deposit(5000)

println(account.current)

account.withdraw(300)

println(account.current)
