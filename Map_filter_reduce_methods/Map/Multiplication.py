def multiplication(n):
    return n * n


# All numbers are doubled using map()
numbers = (1, 2, 3, 4)
result = map(multiplication, numbers)
print(list(result))

# ie, map will apply the operation inside function addition to the list of numbers