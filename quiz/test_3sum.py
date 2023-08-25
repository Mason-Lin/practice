class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        nums.sort()
        for i, num in enumerate(nums):
            target = -num

            # when num is X, target is -X, record expected pair: {target-nums[k]: nums[k]}
            record = {}

            for k in range(i + 1, len(nums)):
                diff = target - nums[k]
                if nums[k] in record:
                    ans = [num, nums[k], record[nums[k]]]
                    if ans not in sol:
                        # print("match", sol)
                        sol.append(ans)

                record[diff] = nums[k]
                # print("target", t, "curr", nums[k], "diff", diff, d)
        return sol


def test_it():
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]

    result = list(reversed([sorted(ans) for ans in Solution().threeSum(nums)]))
    assert result == expected
