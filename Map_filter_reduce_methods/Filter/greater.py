def myfunc(n):
    if n>5:
        return n

data =[9,3,6,4,7,2,1,8,10]
output = filter(myfunc,data)
print(list(output))