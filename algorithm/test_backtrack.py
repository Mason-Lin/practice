# 39. Combination Sum https://leetcode.com/problems/combination-sum/description/


class Solution1:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, [*path, nums[i]], res)


# 40. Combination Sum II https://leetcode.com/problems/combination-sum-ii/description/


class Solution2:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, [*path, nums[i]], res)


# 46. Permutations https://leetcode.com/problems/permutations/description/


class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1 :], [*path, nums[i]], res)


# 47. Permutations II https://leetcode.com/problems/permutations-ii/description/


class Solution4:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res, visited = [], [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, [*path, nums[i]], res)
                visited[i] = False


# 78. Subsets https://leetcode.com/problems/subsets/description/


class Solution5:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, [*path, nums[i]], res)


# 90. Subsets II https://leetcode.com/problems/subsets-ii/description/


class Solution6:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, [*path, nums[i]], res)
