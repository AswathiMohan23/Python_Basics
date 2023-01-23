class Car:
    fuel = "petrol" # class variable

    def __init__(self):
        self.milage =10  #instance variable
        self.company = "ABC" # instance


c1 = Car()
c2 = Car()
c1.milage =8

Car.fuel = "diesel" # need to use class name to modify class variables
print(c1.company, c1.milage, c1.fuel)
print(c2.company,c2.milage,c1.fuel)