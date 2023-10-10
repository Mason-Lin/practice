# https://medium.com/@derekfan/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95-template-binary-tree-divide-conquer-75e5f80f2d21
from collections import OrderedDict
from typing import Optional


class ListNode:
    def __init__(self, val: int, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


# Linked list: fast and slow pointer
def fn1(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next

    return ans


# Reversing a linked list
def fn2(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def linked_list_to_array(linked_list: ListNode):
    array = []
    while linked_list:
        array.append(linked_list.val)
        linked_list = linked_list.next
    return array


def create_linked_list(data) -> ListNode:
    dummy = ListNode(-1)
    curr = dummy
    for val in data:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def insert(head: ListNode, index, data):
    if head is None:
        raise ValueError("empty list")

    if index == 1:
        new_node = ListNode(data)
        new_node.next = head
        return new_node

    cur_idx = 1
    new_node = ListNode(data)
    current_node = head
    while cur_idx + 1 != index:
        current_node = current_node.next
        cur_idx += 1
    new_node.next = current_node.next
    current_node.next = new_node
    return head


def delete(head: ListNode, index):
    if head is None:
        raise ValueError("empty list")

    if index == 1:
        return head.next

    cur_idx = 1
    current_node = head
    while cur_idx + 1 != index:
        current_node = current_node.next
        cur_idx += 1
    current_node.next = current_node.next.next
    return head


def length(head: ListNode):
    if head is None:
        raise ValueError("empty list")

    length = 0
    current_node = head
    while current_node is not None:
        length += 1
        current_node = current_node.next
    return length


def find_middle(head: ListNode):
    if head is None:
        raise ValueError("empty list")

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_node(head: ListNode):
    # less than 2 nodes
    if not head or not head.next:
        return head

    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def copy_random_list(head: ListNode) -> Optional[ListNode]:
    if head is None:
        return head

    # insert cloned
    node = head
    while node:
        original_next = node.next
        # clone
        cloned = ListNode(val=node.val, next=original_next, random=None)
        node.next = cloned

        # next
        node = original_next

    # copy random
    node = head
    while node:
        cloned = node.next
        # copy random
        if node.random is not None:
            cloned.random = node.random.next

        # next
        node = cloned.next

    # split list
    old_curr = head
    new_curr = new_head = head.next
    while old_curr:
        old_curr.next = old_curr.next.next
        if new_curr.next is not None:
            new_curr.next = new_curr.next.next
        old_curr = old_curr.next
        new_curr = new_curr.next
    return new_head


# SC: stack space
def merge_two_lists_rec(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists_rec(list1.next, list2)
        return list1
    list2.next = merge_two_lists_rec(list1, list2.next)
    return list2


def remove_duplicates(head: ListNode) -> Optional[ListNode]:
    if head is None:
        return head

    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return head

    # slow = fast = head
    # while fast:
    #     if fast.val != slow.val:
    #         slow.next = fast
    #         slow = slow.next
    #     fast = fast.next
    # slow.next = None
    # return head


def merge_two_lists(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    cur = dummy = ListNode(-1)

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return dummy.next


# 143. Reorder List
class Solution143:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow.next is the second half head

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev is the second half head

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


def test_143():
    linked_list = create_linked_list([1, 2, 3, 4])
    Solution143().reorderList(linked_list)
    assert linked_list_to_array(linked_list) == [1, 4, 2, 3]

    linked_list = create_linked_list([1, 2, 3, 4, 5])
    Solution143().reorderList(linked_list)
    assert linked_list_to_array(linked_list) == [1, 5, 2, 4, 3]


def test_linked_list():
    # insert
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    linked_list = insert(linked_list, index=1, data=9)
    assert linked_list_to_array(linked_list) == [9, 1, 2, 3, 4, 5]

    linked_list = create_linked_list([1, 2, 3, 4, 5])
    linked_list = insert(linked_list, index=2, data=9)
    assert linked_list_to_array(linked_list) == [1, 9, 2, 3, 4, 5]

    # delete
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    linked_list = delete(linked_list, index=1)
    assert linked_list_to_array(linked_list) == [2, 3, 4, 5]

    linked_list = create_linked_list([1, 2, 3, 4, 5])
    linked_list = delete(linked_list, index=2)
    assert linked_list_to_array(linked_list) == [1, 3, 4, 5]

    # find length
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    assert length(linked_list) == 5

    # find middle
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    assert find_middle(linked_list).val == 3
    linked_list = create_linked_list([1, 2, 3, 4, 5, 6])
    assert find_middle(linked_list).val == 4

    # reverse
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    linked_list = reverse_node(linked_list)
    assert linked_list_to_array(linked_list) == [5, 4, 3, 2, 1]

    # Copy List with Random Pointer
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    cloned_linked_list = copy_random_list(linked_list)
    assert linked_list_to_array(cloned_linked_list) == [1, 2, 3, 4, 5]
    assert cloned_linked_list != linked_list

    # Merge Two Sorted Lists
    linked_list1 = create_linked_list([1, 2, 3, 4, 5])
    linked_list2 = create_linked_list([6, 7, 8, 9])
    merged_linked_list = merge_two_lists_rec(linked_list1, linked_list2)
    assert linked_list_to_array(merged_linked_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    linked_list1 = create_linked_list([1, 2, 3, 4, 5])
    linked_list2 = create_linked_list([6, 7, 8, 9])
    merged_linked_list = merge_two_lists(linked_list1, linked_list2)
    assert linked_list_to_array(merged_linked_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Remove Duplicates from Sorted List
    linked_list = create_linked_list([1, 1, 2, 3, 3])
    assert linked_list_to_array(remove_duplicates(linked_list)) == [1, 2, 3]


# 146. LRU Cache
# Version 1 with OrderedDict
class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


# Version 2 with linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# 138. Copy List with Random Pointer
class Solution138:
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapping = {None: None}
        curr = head
        while curr:
            clone = ListNode(curr.val)
            mapping[curr] = clone
            curr = curr.next
        curr = head
        while curr:
            clone = mapping[curr]
            clone.next = mapping[curr.next]
            clone.random = mapping[curr.random]
            curr = curr.next
        return mapping[head]
