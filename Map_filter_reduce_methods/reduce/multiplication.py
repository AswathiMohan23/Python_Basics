import functools
# importing operator for operator functions
import operator

# initializing list
list = [1, 3, 5, 6, 2]
# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, list))
