# https://hackmd.io/@meyr543/rkjS-x6wY
# https://www.haogroot.com/2020/09/01/monotonic-stack-leetcode/
# stack 存放index。因為存index有很多好處，其中之一就是可以算和target的差距。
# 如果stack為empty則填入-1，也是有利計算差距。


def example(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    st = []

    # 從矩陣尾端往前走訪
    for i in range(len(nums) - 1, -1, -1):
        # 要維持 stack 內都是比新元素還要大, 且越接近 stack bottom 元素
        # 越大, stack top 元素就不能小於要 push 進 stack 的元素, 如果小於就移除 top 元素。
        while st and nums[i] >= nums[st[-1]]:
            st.pop()

        # 當 stack 內為空, 代表找不到比他大的
        # 若 stack 不為空, stack top 元素就是第一個比他大的元素
        ans[i] = -1 if not st else nums[st[-1]]

        # 每個元素一定會被放進 stack
        st.append(i)

    return ans


# Monotonic decreasing stack
def next_greater_element(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        ans[i] = -1 if not stack else nums[stack[-1]]
        stack.append(i)
    return ans


def test_next_greater_element():
    assert next_greater_element([3, 2, 1, 2, 3]) == [-1, 3, 2, 3, -1]
    assert next_greater_element([1, 2, 3, 2, 1]) == [2, 3, -1, -1, -1]
    assert next_greater_element([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
    assert next_greater_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert next_greater_element([1]) == [-1]


# Monotonic increasing stack
def next_smaller_element(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()
        ans[i] = -1 if not stack else nums[stack[-1]]
        stack.append(i)
    return ans


def test_next_smaller_element():
    assert next_smaller_element([3, 2, 1, 2, 3]) == [2, 1, -1, -1, -1]
    assert next_smaller_element([1, 2, 3, 2, 1]) == [-1, 1, 2, 1, -1]
    assert next_smaller_element([1, 2, 3, 4, 5]) == [-1, -1, -1, -1, -1]
    assert next_smaller_element([5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1]
    assert next_smaller_element([1]) == [-1]


# Monotonic decreasing stack
def previous_greater_element(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        ans[i] = -1 if not stack else nums[stack[-1]]
        stack.append(i)
    return ans


def test_previous_greater_element():
    assert previous_greater_element([3, 2, 1, 2, 3]) == [-1, 3, 2, 3, -1]
    assert previous_greater_element([1, 2, 3, 2, 1]) == [-1, -1, -1, 3, 2]
    assert previous_greater_element([1, 2, 3, 4, 5]) == [-1, -1, -1, -1, -1]
    assert previous_greater_element([5, 4, 3, 2, 1]) == [-1, 5, 4, 3, 2]
    assert previous_greater_element([1]) == [-1]


# Monotonic increasing stack
def previous_smaller_element(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()
        ans[i] = -1 if not stack else nums[stack[-1]]
        stack.append(i)
    return ans


def test_previous_smaller_element():
    assert previous_smaller_element([3, 2, 1, 2, 3]) == [-1, -1, -1, 1, 2]
    assert previous_smaller_element([1, 2, 3, 2, 1]) == [-1, 1, 2, 1, -1]
    assert previous_smaller_element([1, 2, 3, 4, 5]) == [-1, 1, 2, 3, 4]
    assert previous_smaller_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert previous_smaller_element([1]) == [-1]
