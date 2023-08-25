# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# from collections import namedtuple
from itertools import count
from queue import PriorityQueue
from typing import NamedTuple, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Item(NamedTuple):
    val: int
    cnt: int
    node: ListNode


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        q = PriorityQueue()
        cnt = count()

        for node in lists:
            if node:
                q.put(Item(node.val, next(cnt), node))

        while q.qsize() > 0:
            item: Item = q.get()
            curr.next = item.node
            curr = curr.next
            if curr.next:
                q.put(Item(curr.next.val, next(cnt), curr.next))

        return dummy.next


def test_it():
    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))
    output = Solution().mergeKLists([a, b, c])
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

    while output:
        assert output.val == expected.val
        output = output.next
        expected = expected.next
