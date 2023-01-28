def myfunc(a):
    return len(a)


data = ('apple','orange','grapes')
x=map(myfunc,data)
print("length of the words : ")
print(list(x))