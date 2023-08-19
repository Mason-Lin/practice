"""https://docs.python.org/zh-tw/3.10/library/queue.html."""
import queue

import pytest


def test_all():
    stack = queue.LifoQueue(maxsize=3)
    stack.put(1)
    stack.put(2)
    stack.put(3)

    with pytest.raises(queue.Full):
        stack.put(4, timeout=0)
    with pytest.raises(queue.Full):
        stack.put_nowait(4)

    assert stack.get() == 3
    assert stack.get() == 2
    assert stack.get() == 1
