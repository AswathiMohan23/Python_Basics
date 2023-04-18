# Find the Highest Integer in the List Using Recursion
#
# Create a function that finds the highest integer in the list using recursion.
# Examplesfind_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
#
# find_highest([0, 12, 4, 87]) ➞ 87
#
# find_highest([8]) ➞ 8
# ===========================================================================================


def swap(question_list, j, param):
    temp = question_list[j + 1]
    question_list[j + 1] = question_list[j]
    question_list[j] = temp


def bubbleSort(question_list, length_of_list):
    for j in range(length_of_list - 1):
        if question_list[j] > question_list[j + 1]:
            swap(question_list, j, j + 1)

    if length_of_list - 1 > 1:
        bubbleSort(question_list, length_of_list-1)


if __name__ == '__main__':
    questionList = [ 3, 5, 6,12, 2]
    length_of_list = len(questionList)
    bubbleSort(questionList, length_of_list)
    print(questionList)
    print("highest no = ",questionList[length_of_list-1])
    print("smallest no = ",questionList[0])
