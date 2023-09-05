class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for left in range(len(numbers) -1):
            right = len(numbers) - 1
            while left < right:
                temp_sum = numbers[left] + numbers[right]
                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left +=1
                else:
                    return [left+1, right+1]

def test_it():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
