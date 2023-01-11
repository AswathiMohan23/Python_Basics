value = 0
print("the numbers are : ")
while value < 10:
    value = value + 1
    if value == 4:
        continue  # here since continue is given this iteration will be skipped
        # and we won't get 4 in the output
    print(value)
