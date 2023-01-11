
def addition(firstNum, secondNum):
    result = firstNum + secondNum

    def printing():
        print("The sum = ", result)
    printing()


firstNo = int(input("Enter the firstNo : "))
secondNo = int(input("Enter the secondNo : "))
addition(firstNo, secondNo)
