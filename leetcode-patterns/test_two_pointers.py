from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


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
        exists = defaultdict(int)
        count = 0
        for num in nums:
            diff = k - num
            if exists[diff] > 0:
                count += 1
                exists[diff] = max(0, exists[diff] - 1)
            else:
                exists[num] += 1
        return count


def test_1679():
    assert Solution1679().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
    assert Solution1679().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1


# 344. Reverse String
class Solution344:
    def reverseString(self, s: list[str]) -> None:
        """Do not return anything, modify s in-place instead."""
        left, right = 0, len(s) - 1
        while left < right:
            # swap
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


# 27. Remove Element
class Solution27:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


# 26. Remove Duplicates from Sorted Array
class Solution26:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


# 83. Remove Duplicates from Sorted List
class Solution83:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


# 5. Longest Palindromic Substring
