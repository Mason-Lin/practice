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
