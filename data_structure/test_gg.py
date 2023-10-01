class Solution2871:
    def maximumTripletValue(self, nums: list[int]) -> int:
        prev_biggest = [float("-inf")] * len(nums)
        post_biggest = [float("-inf")] * len(nums)
        maximun = float("-inf")

        biggest = float("-inf")
        for i in range(len(nums)):
            prev_biggest[i] = biggest
            biggest = max(biggest, nums[i])

        biggest = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            post_biggest[i] = biggest
            biggest = max(biggest, nums[i])

        for j in range(1, len(nums) - 1):
            maximun = max(maximun, (prev_biggest[j] - nums[j]) * post_biggest[j])
        return max(maximun, 0)


def test_2871():
    assert Solution2871().maximumTripletValue([6, 11, 12, 12, 7, 9, 2, 11, 12, 4, 19, 14, 16, 8, 16]) == 190
    assert Solution2871().maximumTripletValue([10, 13, 6, 2]) == 14


class Solution2875:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        nums = nums + nums

        dic = {0: -1}  # accu : index

        base = target // total * n
        target = target % total

        ans = float("inf")
        accu = 0
        for i in range(len(nums)):
            accu += nums[i]
            dic[accu] = i

            if accu - target in dic:
                ans = min(ans, i - dic[accu - target] + base)
        if ans == float("inf"):
            ans = -1
        return ans


def test_2875():
    assert Solution2875().minSizeSubarray([1, 2, 3], 5) == 2
    assert Solution2875().minSizeSubarray([1, 1, 1, 2, 3], 4) == 2
    assert Solution2875().minSizeSubarray([2, 4, 6, 8], 3) == -1
    assert Solution2875().minSizeSubarray([2, 1, 5, 7, 7, 1, 6, 3], 39) == 9

