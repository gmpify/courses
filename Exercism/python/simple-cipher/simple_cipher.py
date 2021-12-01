import random
import string

class Cipher:
    def __init__(self, key=None):
        if not key:
            key = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
        self.key = key
        self.base = ord('a')

    def encode(self, text):
        encoded = []

        for i in range(len(text)):
            plain_shift = ord(text[i]) - self.base
            key_shift = ord(self.key[i % len(self.key)]) - self.base
            encoded_shift = (plain_shift + key_shift) % 26

            encoded.append(chr(encoded_shift + self.base))

        return ''.join(encoded)

    def decode(self, text):
        decoded = []

        for i in range(len(text)):
            encoded_shift = ord(text[i]) - self.base
            key_shift = ord(self.key[i % len(self.key)]) - self.base
            plain_shift = (encoded_shift - key_shift) % 26

            decoded.append(chr(plain_shift + self.base))

        return ''.join(decoded)
