def myfunc(n):
    return n.upper()


data ="hello world"
output = map(myfunc,data)
for i in output:
    print(i,end='')