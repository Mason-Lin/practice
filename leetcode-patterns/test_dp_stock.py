# https://labuladong.github.io/algo/di-ling-zh-bfe1b/yi-ge-fang-3b01b/
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
