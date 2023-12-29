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
