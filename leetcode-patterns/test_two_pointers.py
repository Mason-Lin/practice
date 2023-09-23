from collections import defaultdict


# 283. Move Zeroes
class Solution283:
    def moveZeroes(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
            fast += 1


def test_283():
    nums = [0, 1, 0, 3, 12]
    Solution283().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


# 392. Is Subsequence
class Solution392:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow, fast = 0, 0

        if s in ("", t):
            return True

        while fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1

            if slow == len(s):
                return True
        return False


def test_392():
    assert Solution392().isSubsequence(s="abc", t="ahbgdc") is True
    assert Solution392().isSubsequence(s="axc", t="ahbgdc") is False


# 11. Container With Most Water
class Solution11:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1

        def calc_area(left, right):
            return min(height[left], height[right]) * (right - left)

        max_area = 0
        while left < right:
            max_area = max(max_area, calc_area(left, right))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def test_11():
    assert Solution11().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution11().maxArea(height=[1, 1]) == 1


# 1679. Max Number of K-Sum Pairs
class Solution1679:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # time O(n) / space O(n)
        seems = defaultdict(int)
        count = 0
        for num in nums:
            looking = k - num
            if seems[looking] > 0:
                count += 1
                seems[looking] = max(0, seems[looking] - 1)
            else:
                seems[num] += 1
        return count


def test_1679():
    assert Solution1679().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
    assert Solution1679().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
