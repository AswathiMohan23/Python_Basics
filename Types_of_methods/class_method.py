class Animals:
    home='zoo'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def animals_home(cls,home):
        cls.home=home

animal1=Animals("Lion",4)
print("the original animal home : ",animal1.home)
Animals.animals_home("Jungle")
print("new animal home : ",animal1.home)

