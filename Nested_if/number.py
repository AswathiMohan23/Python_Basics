number=int(input("enter a number between 1 to 100 : "))
if number>=1 and number<=100:
    if number>50:
        print("the entered number is between 1 -100 and is greater than 50")
    elif number<50:
        print("the entered number is between 1 -100 and is less than 50")
    else:
        print("the entered number is between 1 -100 and is equal to 50")

else:
    print("the entered number is not in the specified range")

