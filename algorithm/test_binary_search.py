"""[Python] Powerful Ultimate Binary Search Template. Solved many problems."""
# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.


# Most Generalized Binary Search
def binary_search(array, target) -> int:
    left, right = min(array), max(array)  # could be [0, n], [1, n] etc. Depends on problem

    def condition(mid) -> bool:
        if array[mid] > target:
            return True
        return False

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


# when miss
def binary_search_with_miss(array, target) -> int:
    left, right = min(array), max(array)  # could be [0, n], [1, n] etc. Depends on problem

    def condition(mid) -> bool:
        if array[mid] > target:
            return True
        return False

    while left < right:
        mid = (left + right) >> 1
        if condition(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left if array[left] == target else -1


# Tips:
# Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
# Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
# Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

# when to use it?
# If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.


def test_all():
    # search_space = [1, 2, 3, 4, 4, 4, 5, 6, 7]
    search_space = [1, 2, 3, 4, 4, 4, 6, 7, 8]
    #                        ^        ^
    #                        |        |
    target = 5
    # assert bisect_left(search_space, target) == 3

    # assert bisect_right(search_space, target) == 6
    # assert binary_search(search_space, target) == 6
    # assert binary_search_with_miss(search_space, target) == 6

    # assert bisect_left(search_space, target) == -1
    # assert bisect_right(search_space, target) == -1
    # assert binary_search(search_space, target) == -1
    assert binary_search_with_miss(search_space, target) == -1
