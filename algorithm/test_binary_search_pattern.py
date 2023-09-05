def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def left_bound(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left < 0 or left >= len(arr) or arr[left] != target:
        return -1
    return left


def right_bound(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            left = mid + 1
    if right < 0 or right >= len(arr) or arr[right] != target:
        return -1
    return right


def test_three_kind():
    search_space = [1, 2, 3, 3, 3, 4, 5, 6]

    assert binary_search(search_space, 7) == -1
    assert binary_search(search_space, 2) == 1

    assert left_bound(search_space, 7) == -1
    assert left_bound(search_space, 3) == 2

    assert right_bound(search_space, 7) == -1
    assert right_bound(search_space, 3) == 4
