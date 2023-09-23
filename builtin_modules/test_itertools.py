"""https://docs.python.org/3/library/itertools.html."""
import itertools


def test_all():
    nums = [-1, 0, 1, 2, -1, -4]

    from_itertools = []
    for i, j in itertools.combinations(range(len(nums)), 2):
        from_itertools.append([i, j])

    from_for_loops = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            from_for_loops.append([i, j])

    assert from_itertools == from_for_loops

    cnt = itertools.count()
    assert next(cnt) == 0
    assert next(cnt) == 1

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    b = [1, 0, 1, 0, 1]
    assert list(itertools.islice(itertools.count(), 5)) == [0, 1, 2, 3, 4]

    assert list(itertools.accumulate(x)) == [1, 3, 6, 10, 15]

    assert list(itertools.chain(x, y)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == [*x, *y]

    assert list(itertools.compress("ABCDE", b)) == ["A", "C", "E"] == [i for i, j in zip("ABCDE", b) if j]

    assert list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])) == [6, 4, 1]

    assert list(itertools.filterfalse(lambda x: x % 2, range(10))) == [0, 2, 4, 6, 8] == [i for i in range(10) if i % 2 == 0]
