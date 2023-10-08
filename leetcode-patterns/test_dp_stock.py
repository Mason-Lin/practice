# https://labuladong.github.io/algo/di-ling-zh-bfe1b/yi-ge-fang-3b01b/

# 【背包九讲专题】 https://www.bilibili.com/video/BV1qt411Z7nE/?share_source=copy_web
# https://zhuanlan.zhihu.com/p/139368825


# https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/
# how to find dp solution?
# Find recursive relation
# Recursive (top-down)
# Recursive + memo (top-down)
# Iterative + memo (bottom-up)
# Iterative + N variables (bottom-up)


STATE_FOR_WHOLE_INPUT = None
RECURRENCE_RELATION = None
BASE_CASE = None


# Dynamic programming: top-down memoization
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0

        if STATE in memo:
            return memo[STATE]

        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)
