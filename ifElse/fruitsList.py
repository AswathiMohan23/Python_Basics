fruitList = ['apple', 'orange', 'Mango', 'kiwi', 'grapes']
fruit = input("Enter the name of a fruit : ")
if fruit in fruitList:
    print(fruit, " is present in the given list ", fruitList)
else:
    print(fruit, " is not present in the given list ", fruitList)
