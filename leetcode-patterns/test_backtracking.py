# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-56e11/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-a5f2f/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-9e939/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-89170/
from collections import Counter

BASE_CASE = None
ITERATE_OVER_INPUT = range(10)
OTHER_ARGUMENTS = None


# template
def backtrack(curr, OTHER_ARGUMENTS):
    if BASE_CASE:
        # modify the answer
        return None

    ans = 0
    for _i in ITERATE_OVER_INPUT:
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS)
        # undo the modification of the current state

    return ans


# 39. Combination Sum
class Solution39:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.nums = candidates
        self.nums.sort()
        self.ans = []
        self.backtracking(target, 0, [])
        return self.ans

    def backtracking(self, target: int, index: int, path: list):
        # add ans
        if target == 0:
            self.ans.append(path.copy())
            return
        # no ans, no need deeper
        if target < 0:
            return
        # search deeper
        for i in range(index, len(self.nums)):
            path.append(self.nums[i])
            self.backtracking(target - self.nums[i], i, path)
            path.pop()


# 40. Combination Sum II
class Solution40:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.nums = candidates
        self.nums.sort()
        self.ans = []
        self.backtracking(target, 0, [])
        return self.ans

    def backtracking(self, target: int, index: int, path: list) -> list:
        if target == 0:
            self.ans.append(path.copy())
            return
        if target < 0:
            return
        for i in range(index, len(self.nums)):
            if i > index and self.nums[i] == self.nums[i - 1]:
                continue
            path.append(self.nums[i])
            self.backtracking(target - self.nums[i], i + 1, path)
            path.pop()


# 216. Combination Sum III
class Solution216:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.nums = list(range(1, 10))
        self.size_limit = k
        self.ans = []
        self.backtracking(n, 0, [])
        return self.ans

    def backtracking(self, target, index, path):
        if target == 0 and self.size_limit == len(path):
            self.ans.append(path.copy())
            return
        if target < 0:
            return
        for i in range(index, len(self.nums)):
            path.append(self.nums[i])
            self.backtracking(target - self.nums[i], i + 1, path)
            path.pop()


# 46. Permutations
class Solution46:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.nums.sort()
        self.ans = []
        counter = Counter(self.nums)
        self.backtracking(counter, [])
        return self.ans

    def backtracking(self, counter, path):
        # Base case
        if len(self.nums) == len(path):
            self.ans.append(path.copy())
            return

        for num in counter:
            if counter[num] > 0:
                path.append(num)
                counter[num] -= 1
                self.backtracking(counter, path)
                path.pop()
                counter[num] += 1


# 47. Permutations II
class Solution47:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.nums.sort()
        self.ans = []
        counter = Counter(self.nums)
        self.backtracking(counter, [])
        return self.ans

    def backtracking(self, counter, path):
        # Base case
        if len(self.nums) == len(path):
            self.ans.append(path.copy())
            return

        for num in counter:
            if counter[num] > 0:
                path.append(num)
                counter[num] -= 1
                self.backtracking(counter, path)
                path.pop()
                counter[num] += 1


# 78. Subsets
class Solution78:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.nums.sort()
        self.ans = []
        self.dfs(0, [])
        return self.ans

    def dfs(self, index, path):
        self.ans.append(path.copy())

        for i in range(index, len(self.nums)):
            path.append(self.nums[i])
            self.dfs(i + 1, path)
            path.pop()


# 90. Subsets II
class Solution90:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.nums.sort()
        self.ans = []
        self.backtracking(0, [])
        return self.ans

    def backtracking(self, index, path):
        self.ans.append(path.copy())

        for i in range(index, len(self.nums)):
            if i > index and self.nums[i] == self.nums[i - 1]:
                continue
            path.append(self.nums[i])
            self.backtracking(i + 1, path)
            path.pop()
