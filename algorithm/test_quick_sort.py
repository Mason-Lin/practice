"""quick sort."""


# my best template for quick sort
def partition(arr, left, right):
    i, pivot = left, arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def quick_sort2(arr, head, tail):
    l, r = head, tail
    if l < r:
        m = l + (r - l) // 2
        pivot = arr[m]
        while l <= r:
            while l <= r and arr[l] < pivot:
                l += 1
            while l <= r and arr[r] > pivot:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        quick_sort2(arr, head, r)
        quick_sort2(arr, l, tail)


def test_quick_sort():
    arr = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]

    arr = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort2(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
