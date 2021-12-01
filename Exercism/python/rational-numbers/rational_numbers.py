from __future__ import division
import math

class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.num = int(numer / gcd)
        self.den = int(denom / gcd)

        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    def numer(self):
        return self.num

    def denom(self):
        return self.den

    def __eq__(self, other):
        return self.numer() == other.numer() and self.denom() == other.denom()

    def __repr__(self):
        return '{}/{}'.format(self.numer(), self.denom())

    def __add__(self, other):
        num = self.numer() * other.denom() + self.denom() * other.numer()
        den = self.denom() * other.denom()
        return Rational(num, den)

    def __sub__(self, other):
        num = self.numer() * other.denom() - self.denom() * other.numer()
        den = self.denom() * other.denom()
        return Rational(num, den)

    def __mul__(self, other):
        num = self.numer() * other.numer()
        den = self.denom() * other.denom()
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.numer() * other.denom()
        den = self.denom() * other.numer()
        return Rational(num, den)

    def __abs__(self):
        num = abs(self.numer())
        den = abs(self.denom())
        return Rational(num, den)

    def __pow__(self, power):
        if power >= 0:
            num = self.numer() ** power
            den = self.denom() ** power
            return Rational(num, den)
        else:
            num = self.denom() ** power
            den = self.numer() ** power
            return Rational(num, den)

    def __rpow__(self, base):
        return base ** (self.numer()/self.denom())
