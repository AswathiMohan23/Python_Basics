def str_upper(func):   #decorator
    def inner():
        str1 = print_str()
        return str1.upper()
    return inner
def print_str():
    return "good morning"

print(print_str())

d = str_upper(print_str()) # decorating by passing the
print(d())