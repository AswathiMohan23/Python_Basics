import functools
import operator

a= [1,2,3]
print(functools.reduce(operator.add, a))

