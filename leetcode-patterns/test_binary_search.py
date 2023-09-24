"""[Python] Powerful Ultimate Binary Search Template. Solved many problems.

Tips:

Correctly initialize the boundary variables left and right to specify search space.
    Only one rule: set up the boundary to include all possible elements;
Decide return value. Is it return left or return left - 1?
    Remember this: after exiting the while loop, left is the minimal k satisfying the condition function
Design the condition function.
    This is the most difficult and most beautiful part. Needs lots of practice.
when to use it?
    If we can discover some kind of monotonicity
    for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.
"""
# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/dong-ge-da-334dd/
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/wo-xie-le--3c789/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def special_condition_passed(mid):
    pass


def condition_passed(mid):
    pass


def bs_pattern(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if special_condition_passed(mid):  # (optional)
            return mid
        if condition_passed(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


def binary_search_find_target(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search_find_condition(arr, target) -> int:
    left, right = 0, len(arr) - 1

    def condition(mid) -> bool:
        if arr[mid] >= target:
            return True
        return False

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    # optional, check if left boundary is valid
    return left if condition(left) else -1


def test_hit_or_miss():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                        ^
    assert binary_search_find_target(search_space, 4) == 3
    assert binary_search_find_target(search_space, 5) == -1
    assert binary_search_find_target(search_space, 6) == 4


def test_nearest():
    search_space = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    #                           ^ condition is nums[index] >= target
    assert binary_search_find_condition(search_space, 4) == 3
    assert binary_search_find_condition(search_space, 5) == 4
    assert binary_search_find_condition(search_space, 6) == 4


# 450. Delete Node in a BST
class Solution450:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left

            if not root.left:
                return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


# 700. Search in a Binary Search Tree
class Solution700:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def binary_search(root):
            if root is None:
                return None

            if root.val == val:
                return root

            if root.val > val:
                return binary_search(root.left)

            if root.val < val:
                return binary_search(root.right)

        return binary_search(root)


# 34. Find First and Last Position of Element in Sorted Array
class Solution34:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def left_bound(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid - 1
            if left < 0 or left >= n or nums[left] != target:
                return -1
            return left

        def right_bound(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid + 1
            if right < 0 or right >= n or nums[right] != target:
                return -1
            return right

        return [left_bound(nums, target), right_bound(nums, target)]


def test_34():
    assert Solution34().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert Solution34().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert Solution34().searchRange(nums=[], target=0) == [-1, -1]
