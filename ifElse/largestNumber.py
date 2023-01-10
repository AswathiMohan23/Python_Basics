firstNo = int(input("Enter the first No : "))
secondNo = int(input("Enter the second No : "))
thirdNo = int(input("Enter the third No : "))
if firstNo > secondNo and firstNo > thirdNo:
    print(firstNo, " is the largest number")
elif secondNo > firstNo and secondNo > thirdNo:
    print(secondNo, " is the largest number")
else:
    print(thirdNo, " is the largest number")

