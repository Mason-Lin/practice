# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-56e11/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-a5f2f/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-9e939/
# https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-89170/

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
