# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-56e11/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-a5f2f/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-9e939/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-89170/
from collections import Counter

"""
訣竅:
Subset: 用index避免走回頭路, 遇到有重複的數字, 跳過重複的數字
Combination Sum: 用index避免走回頭路, 遇到有重複的數字, 跳過重複的數字, target紀錄剩餘的目標數字
Permutations: 用一個 counter 來記錄每個數字出現的次數, 每次從counter選擇一個數字, 就把 counter 減一, 遞迴下去, 遞迴回來後, 再把 counter 加回來。
"""


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
        res = []

        def backtracking(target, index, path):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtracking(target - candidates[i], i, path)
                path.pop()

        backtracking(target, 0, [])
        return res


# 40. Combination Sum II
class Solution40:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtracking(target, index, path):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtracking(target - candidates[i], i + 1, path)
                path.pop()

        backtracking(target, 0, [])
        return res


# 216. Combination Sum III
class Solution216:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtracking(target, index, path):
            if target == 0 and len(path) == k:
                res.append(path.copy())
                return
            if target < 0:
                return

            for i in range(index, 10):
                path.append(i)
                backtracking(target - i, i + 1, path)
                path.pop()

        backtracking(n, 1, [])
        return res


# 46. Permutations
class Solution46:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        counter = Counter(nums)

        def backtracking(path):
            if len(path) == len(nums):
                res.append(path.copy())
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtracking(path)
                    path.pop()
                    counter[num] += 1

        backtracking([])
        return res


# 47. Permutations II
class Solution47:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        counter = Counter(nums)

        def backtracking(path):
            if len(path) == len(nums):
                res.append(path.copy())
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtracking(path)
                    path.pop()
                    counter[num] += 1

        backtracking([])
        return res


# 78. Subsets
class Solution78:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtracking(index, path):
            res.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res


# 90. Subsets II
class Solution90:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtracking(index, path):
            res.append(path.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res
