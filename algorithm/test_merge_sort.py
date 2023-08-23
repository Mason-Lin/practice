# """merge sort but not in-place."""


def merge(l, r):
    i, j = 0, 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    return result + l[i:] + r[j:]


# my merge sort template
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    return merge(l, r)


def test_merge_sort():
    array = [8, 7, 1, 4, 5, 2, 3, 6]
    assert merge_sort(array) == [1, 2, 3, 4, 5, 6, 7, 8]

    array = [7, 1, 4, 5, 2, 3, 6]
    assert merge_sort(array) == [1, 2, 3, 4, 5, 6, 7]

    array = [2, 3, 1]
    assert merge_sort(array) == [1, 2, 3]
