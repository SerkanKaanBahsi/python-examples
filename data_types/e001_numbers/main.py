import decimal
import fractions
import math
import random

number = 3

print(type(number))
print(type(4.3))
print(type(4+3j))
print(isinstance(number, int))

print(0b10110)
print(0o12)
print(0xFF)

print(float(number))

# Decimal
print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(2.4 + 3.2 == 5.6)
print(decimal.Decimal(2.4 + 3.2))

# Fractions
print(fractions.Fraction(3.2))
print(fractions.Fraction(1, 5))
print(fractions.Fraction(2))
print(fractions.Fraction("3.2"))
print(2/fractions.Fraction(3))

# Math
print(math.pi)
print(math.sin(90))
print(math.factorial(0))
print("Random Starts Here")

# Random
array = [1, "a", "c", number, 4]
print(random.randrange(2, 22))
print(random.choice(array))
print(random.choices(array))
random.shuffle(array)
print(array)
print(random.random())
