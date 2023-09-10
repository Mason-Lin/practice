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
    left, right = head, tail
    if left < right:
        pivot = arr[right]
        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        quick_sort2(arr, head, right)
        quick_sort2(arr, left, tail)


def test_quick_sort():
    arr = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]

    arr = [8, 7, 1, 4, 5, 2, 3, 6]
    quick_sort2(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
