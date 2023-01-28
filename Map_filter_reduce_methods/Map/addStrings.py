def myfunc(a,b):
    return a+b


colours = ('red','yellow','green')
data2 = ('cherry','pineapple','watermelon')
output = map(myfunc,(colours),(data2))
print(list(output))