import random
import string

LETTERS_COUNT = 2
DIGITS_COUNT = 3

class Robot:
    def __init__(self):
        self.existing_names = set()
        self.reset()

    def reset(self):
        name = ''.join((random.choice(string.ascii_uppercase) for i in range(LETTERS_COUNT)))
        name += ''.join((random.choice(string.digits) for i in range(DIGITS_COUNT)))

        if name in self.existing_names:
            self.reset()
        else:
            self.name = name
            self.existing_names.add(name)
