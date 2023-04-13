# def square(a):
#     return a * a
#
# result = square(5)
# print(result)


f = lambda a: a * a  # a is the arg passed, a*a is the operation done on the arg
# functions are objects in python so assigned it to f


if __name__ == "__main__":
    result = f(5)
    print(result)