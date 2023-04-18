# This sorting technique repeatedly finds the minimum element and sort it in order.
# During the execution of this algorithm, two subarrays are maintained, the subarray which is already
# sorted, and the remaining subarray which is unsorted. During the execution of Selection Sort for
# every iteration, the minimum element of the unsorted subarray is arranged in the sorted subarray.
# Selection Sort is a more efficient algorithm than bubble sort. Sort has a
# Time-Complexity of O(n2) in the average, worst, and in the best cases.
#
# Example
# Sequence: 7, 2, 1, 6

# Ascending order [ explanation ]
# step1 : it assumes first no as smallest no min_num=7 and compares with the next number ,here 2 < 7 so min_num will become 2
#next it checks the next num and min_num becomes 1 and it continues and it understands that the min_num is 1
# step 2 : it moves min_num to zeroth index by swapping. now we have 2 parts sorted part and unsorted part
# step 3 : takes next num of unsorted part as smallest , min_num=2 and the method continues
#descending order
# same procedure instead of min_value, find max_value


def selectionSort(input_list, size):
    for i in range(size):
        min_value = i
        for j in range(i + 1, size):

            # for minimum element in each loop
            if input_list[j] < input_list[min_value]:
                min_value = j

        # Arranging min at the correct position
        (input_list[i], input_list[min_value]) = (input_list[min_value], input_list[i])


if __name__ == "__main__":
    data = [7, 2, 1, 6]
    size = len(data)
    selectionSort(data, size)
    print('Sorted list in Ascending Order is :')
    print(data)