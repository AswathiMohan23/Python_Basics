alphabet = input("enter the alphabet in small letter : ")
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
    print("Its a vowel")
    if 'a' <= alphabet <= 'j':
        print("the alphabet is vowel and is in the range 'a to j'.....")
    elif 'j' < alphabet <= 'z':
        print("the alphabet is vowel and is in the range 'k to z'.....")

else:
    print("Its not a vowel")
