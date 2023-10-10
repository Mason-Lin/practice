r"""重點整理
stack 存放 index 有好處, 可以計算target的差距
會建立另外一個查表用的 list, 用來存放答案, 並初始化為-1
向右查找的時候, 從尾端開始建立stack
向左查找的時候, 從頭開始建立stack
找較大的元素, 用 Monotonic decreasing stack
找較小的元素, 用 Monotonic increasing stack
建立 Monotonic decreasing stack 的時候, 移除比新元素還要小的元素
建立 Monotonic increasing stack 的時候, 移除比新元素還要大的元素.
向左找較大  \          /  向右找較大
decreasing  \        /   <- decreasing
             \      /    從尾端開始建立stack
              - Me -
             /      \    從尾端開始建立stack
increasing  /        \   <- increasing
向左找較小  /          \  向右找較小.
"""


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


def next_greater_element_forward(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans


def test_next_greater_element_forward():
    assert next_greater_element_forward([3, 2, 1, 2, 3]) == [-1, 3, 2, 3, -1]
    assert next_greater_element_forward([1, 2, 3, 2, 1]) == [2, 3, -1, -1, -1]
    assert next_greater_element_forward([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
    assert next_greater_element_forward([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert next_greater_element_forward([1]) == [-1]


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


# 496. Next Greater Element I
class Solution496:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        result = {}
        for v in nums2:
            while stack and v > stack[-1]:
                result[stack.pop()] = v
            stack.append(v)
        return [result.get(v, -1) for v in nums1]


# 503. Next Greater Element II
class Solution503:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        result = [-1] * len(nums)
        stack = []
        for i, v in enumerate(nums):
            while stack and v > nums[stack[-1]]:
                result[stack.pop()] = v
            stack.append(i)

        for i, v in enumerate(nums):
            while stack and v > nums[stack[-1]]:
                result[stack.pop()] = v
        return result
