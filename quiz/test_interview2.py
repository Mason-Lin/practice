import heapq
from math import inf


def find_largest_odd_integer(nums: list[int]) -> int:
    maxi = -inf  # 9
    heapq.heapify(nums)
    for num in nums:  # [ 7, 9, 2, 10 ]
        if num % 2 != 0:  # 7  9  2  10
            maxi = max(maxi, num)
    return maxi


# -   k is bad name
# -   return should be list or int?
# -   allow to modify list in place?
# -   i'm return smallest
# -   should use builtin nlargest?
def find_largest_odd_integer2(nums: list[int], k: int) -> int:
    maxi = -inf
    nums[:] = [-num for num in nums if num % 2 != 0]
    heapq.heapify(nums)

    for _ in range(k):
        maxi = heapq.heappop(nums)
    return -maxi


def test_it():
    assert find_largest_odd_integer([7, 9, 2, 10]) == 9
    assert find_largest_odd_integer([7]) == 7

    assert find_largest_odd_integer2([7, 9, 2, 10], 1) == 9
    assert find_largest_odd_integer2([-1, 7, 9, 2, 10], 3) == -1
    assert find_largest_odd_integer2([7], 1) == 7
