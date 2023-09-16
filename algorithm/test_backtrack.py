# 39. Combination Sum https://leetcode.com/problems/combination-sum/description/


# 數字可重複使用
class Solution1:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, nums, target, index, path, ans):
        if target < 0:
            return  # backtracking
        if target == 0:
            ans.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, [*path, nums[i]], ans)


# 40. Combination Sum II https://leetcode.com/problems/combination-sum-ii/description/


# 數字不能重複使用
class Solution2:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, nums, target, index, path, ans):
        if target < 0:
            return  # backtracking
        if target == 0:
            ans.append(path)
            return  # backtracking
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, [*path, nums[i]], ans)


# 216. Combination Sum III https://leetcode.com/problems/combination-sum-iii/description/


# 數字不可重複使用且數量有限制
class Solution3:
    def combinationSum3(self, k, n):
        ans = []
        nums = list(range(1, 10))
        self.dfs(nums, k, n, 0, [], ans)
        return ans

    def dfs(self, nums, len_ans, target, index, path, ans):
        if len_ans < 0 or target < 0:
            return
        if len_ans == 0 and target == 0:
            ans.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, len_ans - 1, target - nums[i], i + 1, [*path, nums[i]], ans)


# 46. Permutations https://leetcode.com/problems/permutations/description/
# https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/?envType=list&envId=rgg8b9k2


# 挑過就排除掉
class Solution4:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1 :], [*path, nums[i]], ans)


def test_4():
    nums = [1, 2, 3]
    ans = Solution4().permute(nums)
    assert sorted(ans) == sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
        ]
    )


# 47. Permutations II https://leetcode.com/problems/permutations-ii/description/


class Solution5:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans, visited = [], [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], ans)
        return ans

    def dfs(self, nums, visited, path, ans):
        if len(nums) == len(path):
            ans.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, [*path, nums[i]], ans)
                visited[i] = False


def test_5():
    nums = [1, 1, 2]
    ans = Solution5().permuteUnique(nums)
    assert sorted(ans) == sorted(
        [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1],
        ]
    )


# 78. Subsets https://leetcode.com/problems/subsets/description/


class Solution6:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, 0, [], ans)
        return ans

    def dfs(self, nums, index, path, ans):
        ans.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, [*path, nums[i]], ans)


# 90. Subsets II https://leetcode.com/problems/subsets-ii/description/


class Solution7:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, 0, [], ans)
        return ans

    def dfs(self, nums, index, path, ans):
        ans.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, [*path, nums[i]], ans)
