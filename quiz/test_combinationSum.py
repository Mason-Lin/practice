from collections import Counter
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        seen = []
        def backtracking(temp, result):
            sum_temp = sum(temp)
            if sum_temp == target:
                # 也許result用set就可以
                comb = Counter(temp)
                if comb not in seen:
                    result.append([*temp])
                    seen.append(comb)
                return
            if sum_temp > target:
                return
            for candidate in candidates:
                temp.append(candidate)
                backtracking(temp, result)
                temp.pop()

        result = []
        temp = []
        backtracking(temp, result)
        return result


def test_it():
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
