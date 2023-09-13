class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A.reverse()
        A.append(0)
        carry = 1
        for i, num in enumerate(A):
            temp = num + carry
            A[i] = temp % 10
            carry = temp // 10
        while A[-1] == 0:
            A.pop()
        A.reverse()
        return A

        s = "".join([str(i) for i in A])
        n = int(s) + 1
        return [int(i) for i in str(n)]


def test_it():
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([0, 0, 9]) == [1, 0]
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert Solution().plusOne([0, 3, 7, 6, 4, 0, 5, 5, 5]) == [3, 7, 6, 4, 0, 5, 5, 6]
    assert Solution().plusOne([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1]
