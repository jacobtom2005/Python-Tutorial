class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    # Euclid's Algorithm for GCD
    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Reduce fraction
    def _reduce(self):
        gcd = self._gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd

        # Keep denominator positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    # String representation
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Accessors
    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    # Addition
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Subtraction
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Multiplication
    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Equality
    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    # Less than
    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    # Greater than
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator