// 06.scala
object PlayingCardSuits extends Enumeration {
	val Spades = Value("\u2660")
	val Clubs = Value("\u2663")
	val Hearts = Value("\u2665")
	val Diamonds = Value("\u2666")
}

def isSuitRed(suit: PlayingCardSuits.Value): Boolean = {
	suit == PlayingCardSuits.Hearts || suit == PlayingCardSuits.Diamonds
}
