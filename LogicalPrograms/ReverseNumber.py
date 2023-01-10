reverse = 0

number = 1234
while number != 0:     # first iteration==> number=123
    remainder = number % 10   # reminder=(number%10)= 123%10 = 3
    reverse = reverse * 10 + remainder  # reverse=0*10+3=3 (in first iteration reverse =0)
    number = number // 10           # number=123/10=12
print("Reversed number = ", reverse)
