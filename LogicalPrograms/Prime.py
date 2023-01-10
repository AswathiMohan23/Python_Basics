flag = 0
number = int(input("Enter the number : "))
for i in range(2, number):
    if number % i == 0:
        flag = 1
        break
if number == 1 or number == 0:
    print("Number is neither prime nor composite")
elif flag != 1:
    print("Number is a prime number")
else:
    print("Number is a composite number")







