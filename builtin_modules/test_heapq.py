# https://www.youtube.com/watch?v=pAU21g-jBiE&ab_channel=MichaelSambol

import heapq


def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


def test_heap():
    assert heap_sort([9, 8, 4, 5, 2, 1, 3, 7, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
