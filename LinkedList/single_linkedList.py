class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_between(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_begin(self):
        if self.head is Node:
            print("LL is empty so we can't delete the node")
        else:
            self.head=self.head.ref # to get the reference of second node present in the "next" part of thr first node

    def delete_last(self):
        if self.head is None:
            print("LL is empty so we can't delete the node")
        elif self.head.ref is None: # if linked list has only one node
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_end(5)
LL1.add_between(25,20) #adding 15 after 20
LL1.delete_begin()  # delete the first node
LL1.delete_last()  # delete the first node
LL1.print_LL()
