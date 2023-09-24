# https://medium.com/@derekfan/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95-template-binary-tree-divide-conquer-75e5f80f2d21
from typing import Optional


class ListNode:
    def __init__(self, val: int, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


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


def merge_two_lists_rec(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    list2.next = merge_two_lists(list1, list2.next)
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
    new_node = dummy = ListNode(-1)
    node_1 = list1
    node_2 = list2

    while node_1 and node_2:
        if node_1.val < node_2.val:
            new_node.next = node_1
            node_1 = node_1.next
        else:
            new_node.next = node_2
            node_2 = node_2.next
        new_node = new_node.next
    if node_1:
        new_node.next = node_1
    if node_2:
        new_node.next = node_2
    return dummy.next


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
