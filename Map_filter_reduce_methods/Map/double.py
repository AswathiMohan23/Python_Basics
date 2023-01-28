def double(n):
    return 2*n


# All numbers are doubled using map()
numbers = (100, 2, 3, 4)
result = map(double, numbers)
print(list(result))

# ie, map will apply the operation inside function addition to the list of numbers