# pylint: disable=C0200
class Solution:
    def fourSum(self, nums: list[int], four_sum_target: int) -> list[list[int]]:
        # two pointers
        nums.sort()
        results = []
        four_sum_target = 0

        for i in range(len(nums) - 3):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                three_sum_target = four_sum_target - nums[i]

                for j in range(i + 1, len(nums) - 2):
                    if j == 0 or (j > 0 and nums[j - 1] != nums[j]):
                        two_sum_target = three_sum_target - nums[j]

                        # two sum
                        left = i + 1
                        right = len(nums) - 1
                        while left < right:
                            s = nums[left] + nums[right]
                            if s == two_sum_target:
                                results.append((nums[i], nums[j], nums[left], nums[right]))
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


def test_it():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    result = (sorted(ans) for ans in Solution().fourSum(nums, target))
    assert sorted(result) == sorted(expected)
