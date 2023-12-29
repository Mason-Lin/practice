import itertools
from functools import cache


class Solution1531:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def dp(idx, last_char, last_char_count, k):
            if k < 0:
                return float("inf")
            if idx == n:
                return 0
            delete_char = dp(idx + 1, last_char, last_char_count, k - 1)
            if s[idx] == last_char:
                keep_char = dp(idx + 1, last_char, last_char_count + 1, k) + (last_char_count in [1, 9, 99])
            else:
                keep_char = dp(idx + 1, s[idx], 1, k) + 1
            return min(keep_char, delete_char)

        return dp(0, "", 0, k)


def test_1531():
    assert Solution1531().getLengthOfOptimalCompression(s="aaabcccd", k=2) == 4
    assert Solution1531().getLengthOfOptimalCompression(s="aabbaa", k=2) == 2
    assert Solution1531().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0) == 3


class Solution1531_followup:
    def getOptimalCompression(self, s: str, k: int) -> str:
        n = len(s)

        @cache
        def dp(idx, last_char, last_char_count, k, keep):
            list_keep = list(keep)
            if k < 0:
                return float("inf"), keep
            if idx == n:
                return 0, keep

            list_keep_remove = list_keep.copy()
            list_keep_remove[idx] = "?"
            delete_char, delete_char_keep = dp(idx + 1, last_char, last_char_count, k - 1, tuple(list_keep_remove))
            if s[idx] == last_char:
                keep_char, keep_char_keep = dp(idx + 1, last_char, last_char_count + 1, k, tuple(list_keep))
                keep_char += last_char_count in [1, 9, 99]
            else:
                keep_char, keep_char_keep = dp(idx + 1, s[idx], 1, k, tuple(list_keep))
                keep_char += 1

            if keep_char <= delete_char:
                return keep_char, keep_char_keep
            return delete_char, delete_char_keep

        _count, res = dp(0, "", 0, k, tuple(s))
        cleaned = [c for c in res if c != "?"]

        ans = []
        for c, g in itertools.groupby(cleaned):
            group = list(g)
            ans.append(f"{c}{len(group)}" if len(group) > 1 else c)
        return "".join(ans)


def test_1531_followup():
    assert Solution1531_followup().getOptimalCompression(s="aaabcccd", k=2) == "a3c3"
    assert Solution1531_followup().getOptimalCompression(s="aabbaa", k=2) == "a4"
    assert Solution1531_followup().getOptimalCompression(s="aaaaaaaaaaa", k=0) == "a11"
