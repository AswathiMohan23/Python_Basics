
def reverse(inputNumber):
    reverseNo = 0
    while inputNumber != 0:  # first iteration==> inputNumber=123
        remainder = inputNumber % 10  # reminder=(inputNumber%10)= 123%10 = 3
        reverseNo = reverseNo * 10 + remainder  # reverseNo=0*10+3=3 (in first iteration reverseNo =0)
        inputNumber = inputNumber // 10  # inputNumber=123/10=12
    print("Reversed number = ", reverseNo)


value = 1234
reverse(value)

