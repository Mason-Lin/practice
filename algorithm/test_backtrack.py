# 39. Combination Sum https://leetcode.com/problems/combination-sum/description/


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


# 46. Permutations https://leetcode.com/problems/permutations/description/


class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1 :], [*path, nums[i]], ans)


# 47. Permutations II https://leetcode.com/problems/permutations-ii/description/


class Solution4:
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
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, [*path, nums[i]], ans)
                visited[i] = False


# 78. Subsets https://leetcode.com/problems/subsets/description/


class Solution5:
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


class Solution6:
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
