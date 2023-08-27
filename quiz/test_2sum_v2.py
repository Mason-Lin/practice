class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seem = {}
        for n in numbers:
            if n not in seem:
                seem[n] = True

        i = 0
        while i < len(numbers):
            left = target - numbers[i]
            if left not in seem:
                i += 1
                continue
            j = i + 1
            while j < len(numbers):
                if numbers[j] == left:
                    return [i + 1, j + 1]
                j += 1
            i += 1
        return None


def test_it():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
