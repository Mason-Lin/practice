# Counting sort in Python programming
from collections import Counter, defaultdict


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
        counter[num] -= 1
        result[counter[num]] = num

    return result


def test_counting_sort():
    assert counting_sort([4, 2, 2, 8, 3, 3, 10, 11]) == [2, 2, 3, 3, 4, 8, 10, 11]
    assert counting_sort([1, 5, 8, 2, 2, 9]) == [1, 2, 2, 5, 8, 9]


def count_sort(nums):
    k = max(nums)
    counter = [0] * (k + 1)
    result = [0] * len(nums)

    for i in range(len(nums)):
        counter[nums[i]] += 1

    for i in range(1, k + 1):
        counter[i] += counter[i - 1]

    for i in range(len(nums) - 1, -1, -1):
        counter[nums[i]] -= 1
        result[counter[nums[i]]] = nums[i]
    return result


def test_count_sort():
    assert count_sort([4, 2, 2, 8, 3, 3, 10, 11]) == [2, 2, 3, 3, 4, 8, 10, 11]
    assert count_sort([1, 5, 8, 2, 2, 9]) == [1, 2, 2, 5, 8, 9]


def mason_counting_sort(nums):
    counter = Counter(nums)
    for i in range(min(nums), max(nums) + 1):
        counter[i] += counter[i - 1]
    result = [0] * len(nums)
    for num in reversed(nums):
        counter[num] -= 1
        result[counter[num]] = num
    return result


def test_count_sort_counter():
    assert mason_counting_sort([4, 2, 2, 8, 3, 3, 10, 11]) == [2, 2, 3, 3, 4, 8, 10, 11]
    assert mason_counting_sort([1, 5, 8, 2, 2, 9]) == [1, 2, 2, 5, 8, 9]
