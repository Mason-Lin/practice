"""https://docs.python.org/zh-tw/3.10/library/queue.html."""
import queue

import pytest


def test_all():
    pq = queue.PriorityQueue(maxsize=3)
    pq.put(2)
    pq.put(1)
    pq.put(3)

    with pytest.raises(queue.Full):
        pq.put(4, timeout=0)
    with pytest.raises(queue.Full):
        pq.put_nowait(4)

    assert pq.get() == 1
    assert pq.get() == 2
    assert pq.get() == 3
