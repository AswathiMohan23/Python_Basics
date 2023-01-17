def name_generators():
    lst = ["crow", "sparrow", "parrot", "peacock"]
    for i in lst:
            yield i


for i in name_generators():
    print(i)