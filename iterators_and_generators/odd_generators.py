def odd_generators():
    for i in range(0,10):
        if i % 2 != 0:
            yield i


for i in odd_generators():
    print(i)