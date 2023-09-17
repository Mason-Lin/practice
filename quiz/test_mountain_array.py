# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/description/
class Solution941:
    def validMountainArray(self, arr: List[int]) -> bool:
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
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
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
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
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