class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(root):
    if root is None:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)


def test_it():
    root = Node(1, Node(2), Node(3))
    print_tree(root)
