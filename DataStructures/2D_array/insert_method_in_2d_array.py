def display_output(num_array):
    for i in num_array:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    num_array = [[1, 3, 5, 6], [4, 9, 8, 7], [2, 8, 7], [9, 8, 2, 1, 3]]
    display_output(num_array)
    print("\n\t\tAfter inserting a new array the output is \n")
    num_array.insert(2, [10, 20, 30, 40])
    display_output(num_array)
