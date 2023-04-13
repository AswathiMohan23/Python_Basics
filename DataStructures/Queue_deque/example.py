if __name__ == "__main__":
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')
    queue.append('d')
    queue.append('e')
    print("queue is : ", queue)
    queue.pop()  # remove the last element if index is not specified
    print("queue after executing queue.pop()  : ",queue)
    queue.pop(0)  # removes the element present at the given index
    print("queue after executing queue.pop(0)  : ",queue)
