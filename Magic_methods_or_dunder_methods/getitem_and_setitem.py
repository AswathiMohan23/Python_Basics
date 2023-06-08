# import random as ran
#
#
# class CustomList:
#   def __init__(self, num):
#     self.my_list = [ran.randrange(1, 101, 1) for _ in range(num)]
#
# obj = CustomList(5)
# print(obj)
# print(len(obj))
# print(obj[1])
# for item in obj:
#   print(item)
# # ======================= here without giving dunder methods it will show error (attribute error)


import random as ran

class CustomList:
    def __init__(self, num):
        self.my_list = [ran.randrange(1, 101, 1) for _ in range(num)]

    def __str__(self):
        return str(self.my_list)

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __getitem__(self, index):
        return self.my_list[index]

    def __len__(self):
        return len(self.my_list)


obj = CustomList(5)
print(obj)
print(len(obj))
print(obj[1])
for i in obj:
    print(i)
