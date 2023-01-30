# calculates the product of two elements
import functools


def product(x,y):
    return x*y


result = functools.reduce(product, [2, 5, 3, 7])
print(result)