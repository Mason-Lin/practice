# https://labuladong.github.io/algo/di-ling-zh-bfe1b/bfs-suan-f-463fd/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/ru-he-yong-7333b/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/bfs-suan-f-463fd/
# BFS 可以找到最短距离，但是空间复杂度高，而 DFS 的空间复杂度较低。
# 一般来说在找最短路径的时候使用 BFS，其他时候还是 DFS 使用得多一些。
from collections import deque


# Binary tree: BFS
def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans


# Graph: BFS
START_NODE = None
def fn(graph):
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return ans
