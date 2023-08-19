from collections import Counter


def test_all():
    count = Counter()
    count.update([1, 1, 1, 2, 2, 3])
    assert count[1] == 3
    assert list(count.keys()) == [1, 2, 3]
    assert list(count.values()) == [3, 2, 1]
    key, value = count.most_common()[0]
    assert key == 1
    assert value == 3
