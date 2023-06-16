class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printPreorder(root):
    if root:
        # First print the data of node (root node)
        print(root.val, end=" "),

        # Then recursion on left child
        printPreorder(root.left)

        # Finally recursion on right child
        printPreorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("Preorder traversal of binary tree is")
    printPreorder(root)

#             1
#           /   \
#          2      3
#       /    \
#     4       5
