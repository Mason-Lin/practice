from collections import Counter, defaultdict


def window_needs_shrink():
    pass


def sliding_window(s: str):
    window = {}

    left = 0
    right = 0

    while right < len(s):
        c = s[right]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1

        right += 1

        # update window

        while left < right and window_needs_shrink():
            d = s[left]

            left += 1

            # update window
            if d in window:
                window[d] -= 1


# 643. Maximum Average Subarray I
def max_average_subarray_i(nums: list[int], k: int) -> float:
    cur_sum = max_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        # update window
        cur_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, cur_sum)
    return max_sum / k


def test_643():
    assert max_average_subarray_i([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert max_average_subarray_i([5], 1) == 5.0


# 3. Longest Substring Without Repeating Characters


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cnt = 0
        seems = defaultdict(int)
        for right in range(len(s)):
            # update window
            seems[s[right]] += 1

            # shrink
            while seems[s[right]] > 1:
                # update window
                seems[s[left]] -= 1
                left += 1

            cnt = max(cnt, right - left + 1)
        return cnt


def test_3():
    assert Solution3().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution3().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution3().lengthOfLongestSubstring("pwwkew") == 3


# 438. Find All Anagrams in a String


class Solution438:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        target = Counter(p)
        window = Counter(s[: len(p) - 1])
        ans = []
        left = 0

        for i in range(len(p) - 1, len(s)):
            c = s[i]
            window[c] += 1

            if window == target:
                ans.append(left)

            d = s[left]
            window[d] -= 1

            if window[d] == 0:
                del window[d]
            left += 1

        return ans


def test_438():
    assert Solution438().findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert Solution438().findAnagrams(s="abab", p="ab") == [0, 1, 2]


# 567. Permutation in String
class Solution567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter(s1)
        size = len(s1)

        for i in range(len(s2)):
            if s2[i] in window:
                window[s2[i]] -= 1

            if i >= size and s2[i - size] in window:
                window[s2[i - size]] += 1

            if all(window[c] == 0 for c in window):
                return True
        return False


def test_567():
    assert Solution567().checkInclusion(s1="ab", s2="eidbaooo") is True
    assert Solution567().checkInclusion(s1="ab", s2="eidboaoo") is False
