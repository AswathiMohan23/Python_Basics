class InvalidAgeException(Exception):
    def __init__(self,age,message ="not in range"):
        self.age=age
        self.message=message
        super().__init__(self.message)

age = 15
if age<18:
    raise InvalidAgeException(age)
