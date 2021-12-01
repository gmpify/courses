class Car(val manufacturer: String, val modelName: String, val modelYear: Int) {
	var licensePlate = ""

	def this(manufacturer: String, modelName: String) {
		this(manufacturer, modelName, -1)
	}

	def this(manufacturer: String, modelName: String, licensePlate: String) {
		this(manufacturer, modelName, -1)
		this.licensePlate = licensePlate
	}

	def this(manufacturer: String, modelName: String, modelYear: Int, licensePlate: String) {
		this(manufacturer, modelName, modelYear)
		this.licensePlate = licensePlate
	}
}

val c = new Car("BMW", "118i", 2007, "ML06MUU")
