# https://medium.com/@derekfan/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95-template-binary-tree-divide-conquer-75e5f80f2d21
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def dfs_recursive_inorder(node: Node, result: list):
    # l, m, r
    if node:
        dfs_recursive_inorder(node.left, result)
        result.append(node.val)
        dfs_recursive_inorder(node.right, result)


def dfs_recursive_preorder(node: Node, result: list):
    # m, l, r
    if node:
        result.append(node.val)
        dfs_recursive_preorder(node.left, result)
        dfs_recursive_preorder(node.right, result)


def dfs_recursive_postorder(node: Node, result: list):
    # l, r, m
    if node:
        dfs_recursive_postorder(node.left, result)
        dfs_recursive_postorder(node.right, result)
        result.append(node.val)


# hard to remember!
def dfs_iterative_inorder(root: Node):
    # l, m, r
    if root is None:
        return None

    stack = []
    result = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right
    return result


def dfs_iterative_preorder(root: Node):
    # m, l, r
    if root is None:
        return None

    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def dfs_iterative_postorder(root: Node):
    # l, r, m
    if root is None:
        return None

    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        result.append(node.val)
    return result[::-1]


def recursion_divide_conquer(node: Node) -> int:
    if node is None:
        return 0

    left = recursion_divide_conquer(node.left)
    right = recursion_divide_conquer(node.right)

    return max(left, right) + 1


def test_it():
    # Create a graph given in
    # the above diagram
    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1  3  5   7
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(7)

    # DFS recursive traversal
    result = []
    dfs_recursive_preorder(head, result)
    assert result == [4, 2, 1, 3, 6, 5, 7]
    result = []
    dfs_recursive_inorder(head, result)
    assert result == [1, 2, 3, 4, 5, 6, 7]
    result = []
    dfs_recursive_postorder(head, result)
    assert result == [1, 3, 2, 5, 7, 6, 4]

    # DFS iterative traversal
    assert dfs_iterative_preorder(head) == [4, 2, 1, 3, 6, 5, 7]
    assert dfs_iterative_inorder(head) == [1, 2, 3, 4, 5, 6, 7]
    assert dfs_iterative_postorder(head) == [1, 3, 2, 5, 7, 6, 4]

    assert dfs_iterative_preorder(None) is None
    assert dfs_iterative_inorder(None) is None
    assert dfs_iterative_postorder(None) is None

    assert dfs_iterative_preorder(Node(4)) == [4]
    assert dfs_iterative_inorder(Node(4)) == [4]
    assert dfs_iterative_postorder(Node(4)) == [4]
