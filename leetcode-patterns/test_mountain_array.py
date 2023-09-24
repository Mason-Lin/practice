# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/description/
class Solution941:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        left, right = 0, len(arr) - 1
        while left + 1 < len(arr) and arr[left + 1] > arr[left]:
            left += 1
        while right - 1 >= 0 and arr[right - 1] > arr[right]:
            right -= 1

        return 0 < left == right < len(arr) - 1


# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
class Solution852:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # 0 1 2 3 2 1 0
        n = len(arr)
        left, right = 0, n - 1
        # [3,4,5,1]
        #  l m   r
        #      l

        while left < right:
            mid = left + (right - left) // 2
            # guaranteed to be a mountain array
            # .'.
            # '-.
            # .-'
            if arr[mid] > arr[mid + 1]:  # '-.
                right = mid
            else:  # arr[mid] < arr[mid + 1]
                left = mid + 1
        return left


# 1095. Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/description/
class MountainArray:
    def __init__(self, arr) -> None:
        self.arr = arr.copy()

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution1095:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        # find peak
        arr = mountain_arr
        n = arr.length()
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr.get(mid) > arr.get(mid + 1):
                right = mid
            else:
                left = peak = mid + 1
        # search left
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            # l t m r .-'
            if arr.get(mid) > target:
                right = mid - 1
            # l m t r .-'
            elif arr.get(mid) < target:
                left = mid + 1
            else:
                return mid

        # search right
        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # l t m r '-.
            if arr.get(mid) < target:
                right = mid - 1
            # l m t r '-.
            elif arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        return -1


def test_1095():
    assert Solution1095().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
    assert Solution1095().findInMountainArray(2, MountainArray([1, 5, 2])) == 2
    assert Solution1095().findInMountainArray(2, MountainArray([3, 5, 3, 2, 0])) == 3


# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/description/
class Solution162:
    def findPeakElement(self, nums: list[int]) -> int:
        # binary search work because the conditions
        # 1. nums[-1] = nums[n] = -∞
        # 2. nums[i] != nums[i + 1] for all valid i.
        # 3. return the index to any of the peaks.
        # find peak and return index
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# 1901. Find a Peak Element II
# https://leetcode.com/problems/find-a-peak-element-ii/description/
class Solution1901:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        # because the conditions so we can use binary search
        # 1. no two adjacent cells are equal
        # 2. find any peak
        # 3. entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
        # 4. 1 <= mat[i][j]

        # we use binary to find any peak row
        m, n = len(mat), len(mat[0])
        # 0            n-1
        # mid
        # m-1
        left, right = 0, m - 1  # row number
        while left < right:
            mid = left + (right - left) // 2

            if max(mat[mid]) > max(mat[mid + 1]):
                right = mid
            else:
                left = mid + 1
        return [left, mat[left].index(max(mat[left]))]
