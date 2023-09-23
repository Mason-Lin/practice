"""[Python] Powerful Ultimate Binary Search Template. Solved many problems.

Tips:

Correctly initialize the boundary variables left and right to specify search space.
    Only one rule: set up the boundary to include all possible elements;
Decide return value. Is it return left or return left - 1?
    Remember this: after exiting the while loop, left is the minimal k satisfying the condition function
Design the condition function.
    This is the most difficult and most beautiful part. Needs lots of practice.
when to use it?
    If we can discover some kind of monotonicity
    for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.
"""
# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.


def special_condition_passed(mid):
    pass


def condition_passed(mid):
    pass


def bs_pattern(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if special_condition_passed(mid):  # (optional)
            return mid
        if condition_passed(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


def binary_search_find_target(arr, target):
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


def binary_search_find_condition(arr, target) -> int:
    left, right = 0, len(arr) - 1

    def condition(mid) -> bool:
        if arr[mid] >= target:
            return True
        return False

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    # optional, check if left boundary is valid
    return left if condition(left) else -1


def test_hit_or_miss():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                        ^
    assert binary_search_find_target(search_space, 4) == 3
    assert binary_search_find_target(search_space, 5) == -1
    assert binary_search_find_target(search_space, 6) == 4


def test_nearest():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                           ^ condition is nums[index] >= target
    assert binary_search_find_condition(search_space, 4) == 3
    assert binary_search_find_condition(search_space, 5) == 4
    assert binary_search_find_condition(search_space, 6) == 4


# 這個方法不好，甚至多了一層
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


# 不好的方法
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

    assert binary_search_find_target(search_space, 7) == -1
    assert binary_search_find_target(search_space, 2) == 1

    assert left_bound(search_space, 7) == -1
    assert left_bound(search_space, 3) == 2

    assert right_bound(search_space, 7) == -1
    assert right_bound(search_space, 3) == 4
