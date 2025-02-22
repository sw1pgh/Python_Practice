# Write a Class Vector representing a vector of 3 dimensions. Overload the '+' and '*' operator which calculates
# the sum and dot(.) product of them.
"""
Write __str__() method to print the vector as follows:
7i + 8j + 10k
"""


class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        sum_value = Vector(self.a + other.a, self.b + other.b, self.c + other.c)
        return sum_value

    def __mul__(self, other):
        dot_product = self.a * other.a + self.b * other.b + self.c * other.c
        return dot_product

    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"


Vector_1 = Vector(1, 2, 3)
Vector_2 = Vector(4, 5, 6)
Vector_3 = Vector(7, 8, 9)

print(f"The Sum Value of Vector_1 & Vector_2 is: {Vector_1 + Vector_2}")
print(f"The Dot Product of Vector_1 & Vector_2 is: {Vector_1 * Vector_2}\n")

print(f"The Sum Value of Vector_2 & Vector_3 is: {Vector_2 + Vector_3}")
print(f"The Dot Product of Vector_2 & Vector_3 is: {Vector_2 * Vector_3}")