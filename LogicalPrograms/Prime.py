flag = 0
number = int(input("Enter the number : "))
if number == 0 or number == 1:
    print("Number is neither prime nor composite")
else:
    for i in range(2, number):
        if number % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Number is a prime number")
    elif flag == 1:
        print("Number is a composite number")
