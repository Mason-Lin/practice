# https://labuladong.github.io/algo/di-ling-zh-bfe1b/yi-ge-fang-3b01b/

# 【背包九讲专题】 https://www.bilibili.com/video/BV1qt411Z7nE/?share_source=copy_web
# https://zhuanlan.zhihu.com/p/139368825


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
