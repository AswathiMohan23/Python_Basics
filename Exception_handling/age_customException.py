class InvalidAgeException(Exception):
    def __init__(self,age,message="age not in the specified range"):
        self.age=age
        self.message=message
        super().__init__()

age =10
if age < 18:
    raise InvalidAgeException(age)