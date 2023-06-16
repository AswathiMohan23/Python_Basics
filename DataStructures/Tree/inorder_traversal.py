class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        # First recursion on left child
        printInorder(root.left)

        # Then print the data of node
        print(root.val, end=" "),

        # Now recursion on right child
        printInorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root)

#             1
#           /   \
#          2      3
#       /    \
#     4       5


