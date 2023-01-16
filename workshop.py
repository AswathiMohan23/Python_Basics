tuple_example=(1, 2, 3, 4, 4)
print(tuple_example)

list_example = [1, 2, 3, 4]
list_example.append(5)
list_example.append(6)

print("extend() ===> ",list_example)

print("\n-------------------------------------- number pattern ---------------------------------------")
for i in range (0,7):
    for j in range( 1,i):
        pattern = 0+j
        print(j, end=' ')

    print("\n")



