
# importing functools for reduce()
# reduce() is defined in “functools” module,
# reduce() stores the intermediate result and only returns the final summation value.


import functools

# importing operator for operator functions
import operator

# initializing list
list = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, list))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, list))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["hello", " world"]))