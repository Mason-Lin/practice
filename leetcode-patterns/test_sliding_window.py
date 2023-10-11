from collections import Counter, defaultdict

WINDOW_CONDITION_BROKEN = None


# Sliding window
def fn(arr):
    left = ans = 0

    for _right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans


def window_needs_shrink():
    pass


def sliding_window(s: str, t: str):
    window = defaultdict(int)
    need = defaultdict(int)
    for c in t:
        need[c] += 1

    left, right = 0, 0
    while right < len(s):
        c = s[right]
        right += 1

        # update window
        window[c] += 1

        while left < right and window_needs_shrink():
            d = s[left]
            left += 1

            # update window
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
        length = 0
        left = 0
        window = Counter()
        for right in range(len(s)):
            window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
        return length


def test_3():
    assert Solution3().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution3().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution3().lengthOfLongestSubstring("pwwkew") == 3


# 438. Find All Anagrams in a String
class Solution438:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window = Counter(p)
        ans = []
        size = len(p)

        for i in range(len(s)):
            if s[i] in window:
                window[s[i]] -= 1

            if i >= size and s[i - size] in window:
                window[s[i - size]] += 1

            if all(window[c] == 0 for c in window):
                ans.append(i - size + 1)
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


# 1004. Max Consecutive Ones III
class Solution1004:
    def longestOnes(self, nums: list[int], k: int) -> int:
        window = Counter()
        length = 0
        left = 0

        for i in range(len(nums)):
            # extend
            window[nums[i]] += 1

            # shrink
            while window[0] > k:
                window[nums[left]] -= 1
                left += 1

            length = max(length, i - left + 1)
        return length


def test_1004():
    assert Solution1004().longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
    assert Solution1004().longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10


# 1493. Longest Subarray of 1's After Deleting One Element
class Solution1493:
    def longestSubarray(self, nums: list[int]) -> int:
        window = 1
        left = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                window -= 1

            while window < 0:
                if nums[left] == 0:
                    window += 1
                left += 1
            length = max(length, i - left)
        return length


def test_1493():
    assert Solution1493().longestSubarray(nums=[1, 1, 0, 1]) == 3
    assert Solution1493().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert Solution1493().longestSubarray(nums=[1, 1, 1]) == 2


# 1358 Number of Substrings Containing All Three Characters
class Solution1358:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        window = {c: 0 for c in "abc"}
        res = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while all(window.values()):
                window[s[left]] -= 1
                left += 1
            res += left
        return res


# 1248 Count Number of Nice Subarrays
class Solution1248:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        odd = 0
        count = 0
        total = 0
        for right in range(len(nums)):
            if nums[right] % 2:
                odd += 1
                count = 0
            while odd == k:
                if nums[left] % 2:
                    odd -= 1
                left += 1
                count += 1
            total += count
        return total


# 1234 Replace the Substring for Balanced String
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/solutions/408978/javacpython-sliding-window/comments/367697/
# 1004 Max Consecutive Ones III
class Solution1004:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        window = Counter()
        longest = 0
        for right in range(len(nums)):
            window[nums[right]] += 1

            while window[0] > k:
                window[nums[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


# 930 Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/solutions/186683/c-java-python-sliding-window-o-1-space/
# 992 HARD Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/523136/JavaC++Python-Sliding-Window/
# 904 Fruit Into Baskets
class Solution904:
    def totalFruit(self, fruits: list[int]) -> int:
        window = Counter()
        maximum_total = float("-inf")
        left = 0
        for right in range(len(fruits)):
            window[fruits[right]] += 1

            while len(window.keys()) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1

            total = sum(window.values())
            maximum_total = max(maximum_total, total)
        return maximum_total


# 862 HARD Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/143726/c-java-python-o-n-using-deque/


# 209 Minimum Size Subarray Sum
class Solution209:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        window, left = 0, 0
        res = len(nums) + 1
        for right in range(len(nums)):
            window += nums[right]
            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1
        return res if res != (n + 1) else 0


# 424. Longest Repeating Character Replacement
class Solution424:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        window = Counter()
        for right in range(len(s)):
            window[s[right]] += 1
            while (right - left + 1) - window.most_common()[0][1] > k:
                window[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 567. Permutation in String
class Solution567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter()
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if right >= len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if window == target:
                return True
        return False


# 121. Best Time to Buy and Sell Stock
class Solution121:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
        return max_profit
