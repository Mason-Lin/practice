from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)

    def add_vertex(self, vertex):
        self.graph[vertex] = []
