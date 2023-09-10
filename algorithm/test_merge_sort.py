# """merge sort but not in-place."""


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


# my merge sort template
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def test_merge_sort():
    array = [8, 7, 1, 4, 5, 2, 3, 6]
    assert merge_sort(array) == [1, 2, 3, 4, 5, 6, 7, 8]

    array = [7, 1, 4, 5, 2, 3, 6]
    assert merge_sort(array) == [1, 2, 3, 4, 5, 6, 7]

    array = [2, 3, 1]
    assert merge_sort(array) == [1, 2, 3]
