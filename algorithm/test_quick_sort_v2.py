"""quick sort."""


def partition(array, left, right):
    pivot = (left + right) // 2
    array[right], array[pivot] = array[pivot], array[right]
    i = left
    for j in range(left, right):
        if array[j] <= array[right]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]
    return i


def quick_sort(array, left, right):
    if right <= left:
        return
    q = partition(array, left, right)
    quick_sort(array, left, q - 1)
    quick_sort(array, q + 1, right)


def test_quick_sort():
    array = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 3, 4, 5, 6, 7, 8]
