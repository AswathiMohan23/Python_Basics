class Car:

    def __init__(self):
        self.milage =10  #instance variable
        self.company = "BMW" # instance


c1 = Car()
c2 = Car()
c1.milage =8

print(c1.company, c1.milage)
print(c2.company,c2.milage)