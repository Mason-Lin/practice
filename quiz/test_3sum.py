# pylint: disable=C0200
class Solution:
    def threeSumTwoPointer(self, nums: list[int]) -> list[list[int]]:
        # two pointers
        nums.sort()
        results = []
        three_sum_target = 0

        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                two_sum_target = three_sum_target - nums[i]

                # two sum
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == two_sum_target:
                        results.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        # skip duplicate
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < two_sum_target:
                        left += 1
                    else:
                        right -= 1

        return results

    # BAD!!! time 7200ms
    def threeSumHashTable(self, nums: list[int]) -> list[list[int]]:
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

    result = (sorted(ans) for ans in Solution().threeSumHashTable(nums))
    assert sorted(result) == sorted(expected)

    result = (sorted(ans) for ans in Solution().threeSumTwoPointer(nums))
    assert sorted(result) == sorted(expected)
