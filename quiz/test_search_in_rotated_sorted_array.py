class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1
        # left is starting point

        # def binary_search(nums, left, right, target):
        #     while left <= right:
        #         mid = left + (right - left) // 2

        #         if nums[mid] > target:
        #             right = mid - 1
        #         elif nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             return mid
        #     return -1

        # found_in_left = binary_search(nums, 0, middle - 1, target)
        # found_in_right = binary_search(nums, middle, len(nums) - 1, target)
        # if found_in_left == -1 and found_in_right == -1:
        #     return -1
        # return found_in_left if found_in_left != -1 else found_in_right

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


def test_it():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1


test_it()
