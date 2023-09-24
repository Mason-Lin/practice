# Dijkstra's algorithm
import heapq
from math import inf

n = 0
source = 0


def fn():
    graph = {}
    distances = [inf] * n
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        curr_dist, node = heapq.heappop(heap)
        if curr_dist > distances[node]:
            continue

        for nei, weight in graph[node]:
            dist = curr_dist + weight
            if dist < distances[nei]:
                distances[nei] = dist
                heapq.heappush(heap, (dist, nei))
                heapq.heappush(heap, (dist, nei))
                heapq.heappush(heap, (dist, nei))
