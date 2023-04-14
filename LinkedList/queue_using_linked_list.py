# queue using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:  # first in first out or last in last out
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

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def dequeue(self):  # first in first out
        if self.head is None:
            print("LL is empty so we can't delete the node")
        elif self.head.next is None:  # if linked list has only one node
            self.head = None
        else:
            temp = 0
            n = self.head
            while n.next.next is not None:
                n = n.next
            temp = n.next.data
            n.next = None
            return temp


if __name__ == "__main__":
    obj = Queue()
    obj.enqueue(10)
    obj.enqueue(20)
    obj.enqueue(30)
    obj.enqueue(40)
    obj.enqueue(50)
    obj.traverse()
    print("dequeue() ====> ", obj.dequeue())
    obj.traverse()
