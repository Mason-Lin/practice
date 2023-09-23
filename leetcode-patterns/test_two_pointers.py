# 283. Move Zeroes
class Solution283:
    def moveZeroes(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1


def test_283():
    nums = [0, 1, 0, 3, 12]
    Solution283().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
