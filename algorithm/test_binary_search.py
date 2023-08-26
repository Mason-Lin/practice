"""[Python] Powerful Ultimate Binary Search Template. Solved many problems."""


def basic_binary_search(arr, target):
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


# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
# while(lo < hi) {
#   int mid = lo + (hi - lo) / 2;
#   if(Special condition passed)(optional):
#       return mid;
#   if(condition passed)
#       hi = mid;
#   else
#       lo = mid + 1;
# }
# return lo;
def adv_binary_search(arr, target) -> int:
    left, right = 0, len(arr) - 1

    def condition(mid) -> bool:
        if arr[mid] > target:
            return True
        return False

    while left < right:
        mid = left + (right - left) // 2

        # optional, exactly match
        if arr[mid] == target:
            return mid

        if condition(mid):
            right = mid
        else:
            left = mid + 1

    # optional, check if left boundary is the target
    if arr[left] != target:
        return -1

    return left


# Tips:
# Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
# Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
# Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

# when to use it?
# If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.


def test_hit_or_miss():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                        ^
    assert basic_binary_search(search_space, 4) == 3
    assert basic_binary_search(search_space, 5) == -1
    assert basic_binary_search(search_space, 6) == 4


def test_nearest():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                           ^
    assert adv_binary_search(search_space, 4) == 3
    assert adv_binary_search(search_space, 5) == -1
    assert adv_binary_search(search_space, 6) == 4
