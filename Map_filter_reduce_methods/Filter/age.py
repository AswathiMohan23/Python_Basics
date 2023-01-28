def myFunc(x):
  if x > 18:
    return x


age = [5, 12, 17, 18, 24, 32]

output = filter(myFunc, age)

for x in output:
  print(x)