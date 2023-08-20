"""merge sort in-place."""


def merge_sort(array, left, right):
    if (right - left) <= 1:
        return
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid, right)
    merge(array, left, mid, right)
    return


def merge(array, left, mid, right):
    left_half = [*array[left:mid], float("inf")]
    right_half = [*array[mid:right], float("inf")]
    i, j, k = 0, 0, left
    while k != right:
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1


def test_merge_sort():
    array = [8, 7, 1, 4, 5, 2, 3, 6]
    merge_sort(array, 0, len(array))
    assert array == [1, 2, 3, 4, 5, 6, 7, 8]

    array = [7, 1, 4, 5, 2, 3, 6]
    merge_sort(array, 0, len(array))
    assert array == [1, 2, 3, 4, 5, 6, 7]

    array = [2, 3, 1]
    merge_sort(array, 0, len(array))
    assert array == [1, 2, 3]
