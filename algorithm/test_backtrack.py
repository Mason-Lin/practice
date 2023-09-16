from collections import Counter

import pytest

# 39. Combination Sum https://leetcode.com/problems/combination-sum/description/


# 數字可重複使用
class Solution1:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        return self.dfs(candidates, target, [])

    def dfs(self, nums, target, path):
        if target < 0:
            return []
        if target == 0:
            return [path]
        ans = []
        for i in range(len(nums)):
            ans.extend(self.dfs(nums[i:], target - nums[i], [*path, nums[i]]))
        return ans


@pytest.mark.parametrize(
    ("nums", "target", "expected_ans"),
    [
        ([2, 3, 4], 6, [[2, 2, 2], [2, 4], [3, 3]]),
        ([2, 3, 4], 4, [[4], [2, 2]]),
        ([2, 3, 4], 3, [[3]]),
        ([2], 2, [[2]]),
        ([2], 1, []),
        ([], 1, []),
        ([40], 40, [[40]]),
        ([2], 40, [[2] * 20]),
        (list(range(2, 32)), 1, []),
        (list(range(2, 32)), 6, [[2, 2, 2], [2, 4], [3, 3], [6]]),
    ],
)
def test_1(nums, target, expected_ans):
    actual_ans = Solution1().combinationSum(nums, target)
    assert sorted(expected_ans) == sorted(actual_ans)  # sorted if needed


# 40. Combination Sum II https://leetcode.com/problems/combination-sum-ii/description/


# 數字不能重複使用
class Solution2:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = candidates
        nums.sort()
        return self.dfs(nums, target, [])

    def dfs(self, nums: list, target: int, path: list) -> list:
        if target == 0:
            return [path]
        if target < 0:
            return []
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans.extend(self.dfs(nums[i + 1 :], target - nums[i], [*path, nums[i]]))
        return ans


@pytest.mark.parametrize(
    ("nums", "target", "expected_ans"),
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ],
)
def test_2(nums, target, expected_ans):
    actual_ans = Solution2().combinationSum2(nums, target)
    assert sorted(expected_ans) == sorted(actual_ans)  # sorted if needed


# 216. Combination Sum III https://leetcode.com/problems/combination-sum-iii/description/


# 數字不可重複使用且數量有限制
class Solution3:
    def combinationSum3(self, k, n):
        nums = list(range(1, 10))
        return self.dfs(nums, n, k, [])

    def dfs(self, nums, target, size_limit, path):
        if target == 0 and size_limit == 0:
            return [path]
        if target < 0 and size_limit < 0:
            return []
        ans = []
        for i in range(len(nums)):
            sub_ans = self.dfs(nums[i + 1 :], target - nums[i], size_limit - 1, [*path, nums[i]])
            ans.extend(sub_ans)
        return ans


@pytest.mark.parametrize(
    ("k", "n", "expected_ans"),
    [
        (3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (4, 1, []),
    ],
)
def test_3(k, n, expected_ans):
    actual_ans = Solution3().combinationSum3(k, n)
    assert sorted(expected_ans) == sorted(actual_ans)  # sorted if needed


# 46. Permutations https://leetcode.com/problems/permutations/description/
# https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/?envType=list&envId=rgg8b9k2


# 挑過就排除掉
class Solution4:
    def permute(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        counter = Counter(nums)
        return self.dfs(nums, counter, [])

    def dfs(self, nums, counter, path):
        # Base case
        if len(nums) == len(path):
            return [path]

        ans = []
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                sub_ans = self.dfs(nums, counter, [*path, num])
                ans.extend(sub_ans)
                counter[num] += 1
        return ans

    #     nums.sort()  # nlogn
    #     return self.dfs(nums, [])  # n * n!

    # def dfs(self, nums, path):
    #     if not nums:
    #         return [path]
    #     ans = []
    #     for i in range(len(nums)):
    #         sub_ans = self.dfs(nums[:i] + nums[i + 1 :], [*path, nums[i]])
    #         ans.extend(sub_ans)
    #     return ans


def test_4():
    nums = [1, 2, 3]
    ans = Solution4().permute(nums)
    assert sorted(ans) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]])


# 47. Permutations II https://leetcode.com/problems/permutations-ii/description/


class Solution5:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        counter = Counter(nums)
        return self.dfs(nums, counter, [])

    def dfs(self, nums, counter, path):
        # Base case
        if len(nums) == len(path):
            return [path]

        ans = []
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                sub_ans = self.dfs(nums, counter, [*path, num])
                ans.extend(sub_ans)
                counter[num] += 1
        return ans

    #     ans, visited = [], [False] * len(nums)
    #     nums.sort()
    #     self.dfs(nums, visited, [], ans)
    #     return ans

    # def dfs(self, nums, visited, path, ans):
    #     if len(nums) == len(path):
    #         ans.append(path)
    #         return
    #     for i in range(len(nums)):
    #         if not visited[i]:
    #             if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
    #                 continue
    #             visited[i] = True
    #             self.dfs(nums, visited, [*path, nums[i]], ans)
    #             visited[i] = False


def test_5():
    nums = [1, 1, 2]
    ans = Solution5().permuteUnique(nums)
    assert sorted(ans) == sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])


# 78. Subsets https://leetcode.com/problems/subsets/description/


class Solution6:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # nlogn
        return self.dfs(nums, [])

    def dfs(self, nums, path):
        ans = []
        ans.append(path)  # [[], [1], [2], [1,2], [1,3], [2,3], [1,2,3]]
        for i in range(len(nums)):  # nums[i]:1{2}
            ans += self.dfs(nums[i + 1 :], [*path, nums[i]])
        return ans


def test_6():
    nums = [1, 2, 3]
    ans = Solution6().subsets(nums)
    assert sorted(ans) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


# 90. Subsets II https://leetcode.com/problems/subsets-ii/description/


class Solution7:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        return self.dfs(nums, [])

    def dfs(self, nums, path):
        ans = []
        ans.append(path)
        for i in range(len(nums)):
            # ... skip dup
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans += self.dfs(nums[i + 1 :], [*path, nums[i]])
        return ans


def test_7():
    nums = [1, 2, 2]
    ans = Solution7().subsetsWithDup(nums)
    assert sorted(ans) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
