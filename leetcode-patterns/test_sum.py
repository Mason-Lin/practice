# 1. Two Sum
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash
        exists = {}
        for i, num in enumerate(nums):
            if (target - num) not in exists:
                exists[num] = i
            else:
                return [i, exists[target - num]]


def test_1():
    assert Solution1().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution1().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution1().twoSum(nums=[3, 3], target=6) == [0, 1]


# 167. Two Sum II - Input Array Is Sorted
class Solution167:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:  # two_sum == target
                return [left + 1, right + 1]


def test_167():
    assert Solution167().twoSum(nums=[2, 7, 11, 15], target=9) == [1, 2]
    assert Solution167().twoSum(nums=[2, 3, 4], target=6) == [1, 3]
    assert Solution167().twoSum(nums=[-1, 0], target=-1) == [1, 2]


# 15. 3Sum
class Solution15:
    def threeSumTwoPointer(self, nums: list[int]) -> list[list[int]]:
        # two pointers
        nums.sort()
        results = []
        three_sum_target = 0

        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                two_sum_target = three_sum_target - nums[i]

                # two sum
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == two_sum_target:
                        results.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        # skip duplicate
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < two_sum_target:
                        left += 1
                    else:
                        right -= 1

        return results


def test_15():
    result = (sorted(ans) for ans in Solution15().threeSumTwoPointer(nums=[-1, 0, 1, 2, -1, -4]))
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]])

    result = (sorted(ans) for ans in Solution15().threeSumTwoPointer(nums=[0, 0, 0]))
    assert sorted(result) == sorted([[0, 0, 0]])

    result = (sorted(ans) for ans in Solution15().threeSumTwoPointer(nums=[0, 1, 1]))
    assert sorted(result) == sorted([])


# 16. 3Sum Closest
class Solution16:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # brute
        # nums.sort()
        # n = len(nums)
        # closest = float("inf")
        # best = None
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             s = nums[i] + nums[j] + nums[k]
        #             diff = abs(target - s)
        #             if closest > diff:
        #                 closest = diff
        #                 best = s
        # return best

        # two pointer
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return closest


def test_16():
    assert Solution16().threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2
    assert Solution16().threeSumClosest(nums=[0, 0, 0], target=1) == 0


# 18. 4Sum
class Solution18:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1
                while left < right:
                    two_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if two_sum == target:
                        result.append((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif two_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result


def test_it():
    result = (sorted(ans) for ans in Solution18().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    assert sorted(result) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    result = (sorted(ans) for ans in Solution18().fourSum(nums=[2, 2, 2, 2, 2], target=8))
    assert sorted(result) == sorted([[2, 2, 2, 2]])
    assert sorted(result) == sorted([[2, 2, 2, 2]])
