# pylint: disable=C0200
class Solution:
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
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    result = (sorted(ans) for ans in Solution().fourSum(nums, target))
    assert sorted(result) == sorted(expected)
