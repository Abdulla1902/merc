class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def GCD(self, a, b):
        return (self.GCD(b, a % b) if b else a)

    def add(self, other):
        znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator +\
                znam // other.denumerator * other.numerator
        self.numerator = chisl
        self.denumerator = znam
        return Fraction(numerator=chisl, denumerator=znam)

    def sub(self, other):
        znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator - \
                znam // other.denumerator * other.numerator
        self.numerator = chisl
        self.denumerator = znam
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def mul(self, other):
        chisl = self.numerator * other.numerator
        znam = self.denumerator * other.denumerator
        k = self.GCD(chisl, znam)
        chisl //= k
        znam //= k
        self.numerator = chisl
        self.denumerator = znam
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def floordiv(self, other):
        n = other.numerator
        other.numerator = other.denumerator
        other.denumerator = n
        chisl = self.numerator * other.numerator
        znam = self.denumerator * other.denumerator
        k = self.GCD(chisl, znam)
        chisl //= k
        znam //= k
        self.numerator = chisl
        self.denumerator = znam
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def str(self):
        return f"{self.numerator}/{self.denumerator}"

num1 = input("Введите дробь в формате ?/?: ")
num2 = input("Введите дробь в формате ?/?: ")

num1 = num1.split('/')
num2 = num2.split('/')
# print(num1)
# print(num2)
# print()

a = Fraction(int(num1[0]), int(num1[1]))
b = Fraction(int(num2[0]), int(num2[1]))

print(f"{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {a + b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} - {num2[0]}/{num2[1]} = {a - b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {a * b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} // {num2[0]}/{num2[1]} = {a // b}")