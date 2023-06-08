# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person = Person('Sarah', 25)
print(person) # ==================> with out __str__ method it gives memory location as output

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Person: {}, Age: {}".format(self.name, self.age)

    def __repr__(self):
        print('inside repr')
        return " Person: {}, Age: {}".format(self.name, self.age)

person = Person('Sarah', 25)
print(person)
print(type(person))
print(type('{}'.format(person)))
