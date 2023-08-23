"""quick sort."""


# my best template for quick sort
def partition(arr, l, r):
    i, pivot = l, arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quick_sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, r)


def test_quick_sort():
    arr = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
