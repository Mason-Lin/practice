# Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left, right, prod = 0, 0, 1
        count = 0
        while right < len(nums):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count


def test_it():
    nums = [10, 5, 2, 6]
    k = 100
    assert Solution().numSubarrayProductLessThanK(nums, k) == 8
