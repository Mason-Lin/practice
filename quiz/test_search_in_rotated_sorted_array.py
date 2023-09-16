# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution33:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        # left is starting point

        rot = left
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            real_mid = (mid + rot) % n
            if nums[real_mid] > target:
                right = mid - 1
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                return real_mid

        return -1


def test_33():
    assert Solution33().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution33().search([4, 5, 6, 7, 0, 1, 2], 3) == -1


# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution81:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


def test_81():
    assert Solution81().search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert Solution81().search([2, 5, 6, 0, 0, 1, 2], 3) is False


# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution153:
    def findMin(self, nums: list[int]) -> int:
        return self.binary_search(nums)

    def binary_search(self, nums):
        left, right = 0, len(nums) - 1
        # return the index when nums[index] > nums[index+1]
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                # shrink right boundary
                right = mid
            else:
                left = mid + 1
        return nums[left]


def test_153():
    assert Solution153().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution153().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
