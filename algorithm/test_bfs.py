# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def bfs(head: Node):
    queue = deque()
    queue.append(head)
    result = []
    while queue:
        for _i in range(len(queue)):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def bfs_list(head: Node):
    queue = [head]
    result = []
    for node in queue:
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# Driver code
def test_it():
    # Create a graph given in
    # the above diagram
    #      0
    #    /   \
    #   1     2
    #  / \   / \
    # 3  4  5   6
    head = Node(0)
    head.left = Node(1)
    head.right = Node(2)
    head.left.left = Node(3)
    head.left.right = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)

    # BFS traversal
    assert bfs(head) == [0, 1, 2, 3, 4, 5, 6]
    assert bfs_list(head) == [0, 1, 2, 3, 4, 5, 6]
