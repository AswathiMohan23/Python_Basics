class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:  # last in first out or first in last out
    def __init__(self):
        self.head = None

    def traverse(self):  # get the value of each node
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def push(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def pop(self):  # first in last out
        if self.head is Node:
            print("stack is empty")
        else:
            temp = self.head
            self.head = self.head.next  # to get the reference of 2nd node present in the "next" part of thr 1st node
            return temp.data

    def peek(self):  # gives the first (top) value
        if self.head is None:
            print("stack is empty")
        return self.head.data


if __name__ == "__main__":
    obj = Stack()
    obj.push(10)
    obj.push(20)
    obj.push(30)
    obj.push(40)
    obj.push(50)
    obj.traverse()
    print("pop() ====> ", obj.pop())
    obj.traverse()
    print("peek() ====> ", obj.peek())
