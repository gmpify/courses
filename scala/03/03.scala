val a = Array(1, 2, 3, 4, 5)

val b = for(i <- a.indices)
	yield if (i == (a.length - 1)) {
			a(i)
		}
		else if (i % 2 == 0) {
			a(i + 1)
		}
		else {
			a(i - 1)
		}
	}
