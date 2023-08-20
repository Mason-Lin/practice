"""quick sort but not in place."""


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop()
    left, right = [], []
    for item in array:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return [*quick_sort(left), pivot, *quick_sort(right)]


def test_quick_sort():
    array = [8, 7, 1, 4, 5, 2, 3, 6]
    assert quick_sort(array) == [1, 2, 3, 4, 5, 6, 7, 8]
