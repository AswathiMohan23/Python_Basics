# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...

def fibonacciFunction(firstNo, secondNo, limit):
    for i in range(2, limit):  # already gave 1st and second nos to print and rest is 3 to the limit
        result = firstNo + secondNo
        firstNo = secondNo
        secondNo = result
        print(result)


firstNo = 0
secondNo = 1
limit = int(input("enter the limit : "))
print("The fibonacci sequence is : ")
print(firstNo)
print(secondNo)
fibonacciFunction(firstNo, secondNo, limit)
