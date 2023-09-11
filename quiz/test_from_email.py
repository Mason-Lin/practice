from collections import defaultdict, deque
from typing import Optional


def parentheses(arr):
    count = 0
    for v in arr:
        if v == "(":
            count += 1
        elif v == ")":
            count -= 1
        else:
            raise ValueError("not ( or )")
        if count < 0:
            return False
    return count == 0


def test_parentheses():
    assert parentheses("()") is True
    assert parentheses(")(()))") is False
    assert parentheses("(") is False
    assert parentheses("(())((()())())") is True


def zeros(n):
    # n!
    if n < 0:
        raise ValueError("negative")

    # 5 * 2
    # 10 == 5 * 2
    # 25 == 5 * 5
    # even number * 5(how many)
    # n // 5
    # n // 5**2 25
    # n // 5**3 125
    # n // 5**4 625
    div = 5
    cnt = 0
    while div <= n:
        cnt += n // div
        div *= 5
    return cnt


def test_zeros():
    assert zeros(5) == 1
    assert zeros(6) == 1
    assert zeros(12) == 2
    assert zeros(25) == 6


#     1
# 8        4
#   3        5
#              7
# [1,8,4,3,5,7]


class TreeNode:
    def __init__(self, value):
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.value: int = value


def bfs(root):
    queue = deque()
    queue.append(root)
    result = []
    while len(queue) > 0:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def test_bfs():
    root = TreeNode(1)
    root.left = TreeNode(8)
    root.right = TreeNode(4)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(7)
    assert bfs(root) == [1, 8, 4, 3, 5, 7]


def encode(arr):
    counter = defaultdict(int)
    result = []
    for char in arr:
        counter[char.lower()] += 1

    for char in arr:
        if counter[char.lower()] > 1:
            result.append(")")
        else:
            result.append("(")
    return "".join(result)


def test_encode():
    assert encode("din") == "((("
    assert encode("recede") == "()()()"
    assert encode("Success") == ")())())"
    assert encode("(( @") == "))(("
