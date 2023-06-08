class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string


if __name__ == '__main__':
    string1 = String('Hello')
    print(string1)