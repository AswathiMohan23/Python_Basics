def display_output(num_array):
    for i in num_array:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    num_array = [[1, 3, 5, 6], [4, 0, 8, 7], [2, 8, 7], [9, 8, 2, 1, 3]]
    display_output(num_array)
    print("\n\t\tAfter updating the output is \n")
    num_array[2] = [1, 1, 1, 1]
    num_array[1][2] = 9
    display_output(num_array)
