# 1095 https://leetcode.com/problems/find-in-mountain-array/description/
# Find in Mountain Array


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr) -> None:
        self.arr = arr.copy()

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        def binary_search_highest(arr, left, right) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if mid == 0:
                    left = mid + 1
                    continue
                if mid == (arr.length() - 1):
                    right = mid - 1
                    continue

                before = arr.get(mid - 1)
                current = arr.get(mid)
                after = arr.get(mid + 1)
                # highest point
                if before < current > after:
                    return mid

                # descending
                if before > current > after:
                    right = mid - 1
                # ascending
                elif before < current < after:
                    left = mid + 1
                else:
                    raise ValueError("Invalid mountain array")
            return -1

        highest_index = binary_search_highest(mountain_arr, 0, mountain_arr.length() - 1)

        def binary_search_1(arr, left, right, target) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                current = arr.get(mid)
                if current == target:
                    return mid
                if current > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        ans1 = binary_search_1(mountain_arr, 0, highest_index, target)

        def binary_search_2(arr, left, right, target) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                current = arr.get(mid)
                if current == target:
                    return mid
                if current < target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        ans2 = binary_search_2(mountain_arr, highest_index, mountain_arr.length() - 1, target)

        return ans1 if ans1 != -1 else ans2


assert Solution().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
assert Solution().findInMountainArray(2, MountainArray([1, 5, 2])) == 2
assert Solution().findInMountainArray(2, MountainArray([3, 5, 3, 2, 0])) == 3


class Solution2:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        length = mountain_arr.length()
        # find index of peak
        # If I want find the index, I always use while (left < right)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = peak = mid + 1

        # find target in the left of peak
        # If I may return the index during the search, I'll use while (left <= right)
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                right = mid - 1
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                return mid
        # find target in the right of peak
        left, right = peak, length - 1
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                right = mid - 1
            elif mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        return -1


assert Solution2().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
assert Solution2().findInMountainArray(2, MountainArray([1, 5, 2])) == 2
assert Solution2().findInMountainArray(2, MountainArray([3, 5, 3, 2, 0])) == 3
