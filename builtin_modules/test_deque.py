from collections import deque


def test_all():
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    # d == [1, 2, 3]
    assert queue.pop() == 3
    assert queue.popleft() == 1
    assert len(queue) == 1
    assert queue[0] == 2

    queue.appendleft(1)
    queue.appendleft(0)
    # d == [0, 1, 2]
    queue.rotate(1)
    # d == [2, 0, 1]
    assert queue[0] == 2
    assert queue[1] == 0
    assert queue[2] == 1
    assert queue[2] == 1
