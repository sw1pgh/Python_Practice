from functools import reduce

# Map Example
L = [1, 2, 3, 4, 5]

square_func = lambda x: x * x

sqaured_L = map(square_func, L)

print(list(sqaured_L))


# Filter Example
def even(n):
    if n % 2 == 0:
        return True
    return False


onlyEven = filter(even, L)
print(list(onlyEven))


# Reduce Example
def sum(a, b):
    return a + b

print(reduce(sum, L))