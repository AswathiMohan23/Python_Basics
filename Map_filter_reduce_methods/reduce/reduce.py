
# importing functools for reduce()
# reduce() is defined in “functools” module,
# reduce() stores the intermediate result and only returns the final summation value.


import functools

# importing operator for operator functions
import operator


# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, list))
