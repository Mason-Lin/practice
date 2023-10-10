from collections import deque
from typing import Optional


class Graph1:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)

    def add_vertex(self, vertex):
        self.graph[vertex] = []


def test_it():
    g = Graph1()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    print(g.graph)


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for src, dest in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Perform BFS on the graph starting from vertex `v`
def bfs(graph, v, discovered):
    # create a queue for doing BFS
    q = deque()

    # mark the source vertex as discovered
    discovered[v] = True

    # enqueue source vertex
    q.append(v)

    # loop till queue is empty
    while q:
        # dequeue front node and print it
        v = q.popleft()
        print(v, end=" ")

        # do for every edge (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it as discovered and enqueue it
                discovered[u] = True
                q.append(u)


def test_grpah():
    # List of graph edges as per the above diagram
    edges = [
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (5, 9),
        (5, 10),
        (4, 7),
        (4, 8),
        (7, 11),
        (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]

    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15

    # build a graph from the given edges
    graph = Graph(edges, n)

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            # start BFS traversal from vertex i
            bfs(graph, i, discovered)


# 200. Number of Islands
class Solution200:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def clean_ones(row, col):
            if row in range(ROWS) and col in range(COLS) and (row, col) not in visited:
                visited.add((row, col))
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    clean_ones(row + 1, col)
                    clean_ones(row - 1, col)
                    clean_ones(row, col + 1)
                    clean_ones(row, col - 1)

        island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island += 1
                    clean_ones(r, c)
        return island


def test_200():
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    assert Solution200().numIslands(grid) == 1
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    assert Solution200().numIslands(grid) == 3


# 133. Clone Graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution133:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        mapping = {}

        def dfs(root):
            if root:
                if root not in mapping:
                    mapping[root] = Node(root.val, [])
                    for adj in root.neighbors:
                        mapping[root].neighbors.append(dfs(adj))
                return mapping[root]

        return dfs(node)


# 79. Word Search
class Solution79:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        length = len(word)
        visited = set()

        def backtracking(row: int, col: int, index: int) -> bool:
            if length == index:
                return True
            if not (0 <= row < ROWS) or not (0 <= col < COLS) or word[index] != board[row][col] or (row, col) in visited:
                return False

            # up, down, left, right
            index += 1
            visited.add((row, col))
            match = (
                backtracking(row + 1, col, index)
                or backtracking(row - 1, col, index)
                or backtracking(row, col + 1, index)
                or backtracking(row, col - 1, index)
            )
            visited.remove((row, col))
            return match

        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(r, c, 0):
                    return True
        return False


def test_79():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert Solution79().exist(board, word) is True
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert Solution79().exist(board, word) is True
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    assert Solution79().exist(board, word) is False
