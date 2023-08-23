class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)

    def add_vertex(self, vertex):
        self.graph[vertex] = []


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print(g.graph)
