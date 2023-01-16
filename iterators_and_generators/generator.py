def even_numbers():
    for i in range(10):
        if (i % 2 == 0):
            yield i

        # Successive Function call using for loop


for i in even_numbers():
    print(i)