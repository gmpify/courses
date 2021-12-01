# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses = set()

    def guess(self, char):
        if self.status == STATUS_WIN:
            raise ValueError('Game finished. You won already')
        elif self.status == STATUS_LOSE:
            raise ValueError('Game finished. You have no more remaining guesses')
        
        if (char in self.word and char not in self.guesses):
            self.guesses.add(char)
            if (set(self.word) == self.guesses):
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        masked_word = map(lambda c: c if c in self.guesses else '_', self.word)
        return ''.join(masked_word)

    def get_status(self):
        return self.status
