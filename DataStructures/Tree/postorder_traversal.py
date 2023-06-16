class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printPostorder(root):
    if root:
        # First recursion on left child
        printPostorder(root.left)

        # The recursion on right child
        printPostorder(root.right)

        # Now print the data of node
        print(root.val, end=" "),


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Postorder traversal of binary tree is")
    printPostorder(root)

    #             1
    #           /   \
    #          2      3
    #       /    \
    #     4       5
