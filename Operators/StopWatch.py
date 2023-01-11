from timeit import default_timer as timer

start = timer()
a = 2
b = 1
print("sum = ", a+b)
end = timer()
print(end - start)


