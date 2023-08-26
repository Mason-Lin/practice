# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        if s == t:
            return True

        while j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

            if i == len(s):
                return True

        return False


def test_it():
    assert Solution().isSubsequence("aaaaaa", "bbaaaa") is False
    assert Solution().isSubsequence("abc", "ahbgdc") is True
