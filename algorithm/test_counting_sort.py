# Counting sort in Python programming
from collections import defaultdict


def counting_sort(nums):
    # count frequency
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    # prefix sum
    for i in range(min(nums), max(nums) + 1):
        counter[i] += counter[i - 1]

    # Find the index of each element of the original array in count array
    result = [0] * len(nums)
    for num in reversed(nums):
        result[counter[num] - 1] = num
        counter[num] -= 1

    return result


def test_counting_sort():
    assert counting_sort([4, 2, 2, 8, 3, 3, 10, 11]) == [2, 2, 3, 3, 4, 8, 10, 11]
    assert counting_sort([1, 5, 8, 2, 2, 9]) == [1, 2, 2, 5, 8, 9]
