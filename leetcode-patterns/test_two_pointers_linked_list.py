import heapq
from itertools import count
from typing import Optional


class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


# 141. Linked List Cycle
class Solution141:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# 142. Linked List Cycle II
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None


# 160. Intersection of Two Linked Lists
class Solution160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
        while p != q:
            # if p is None then switch to headB
            p = headB if not p else p.next
            q = headA if not q else q.next
        return p


# 19. Remove Nth Node From End of List
class Solution19:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


# 21. Merge Two Sorted Lists
class Solution21:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = dummy = ListNode(-1)
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next


# 23. Merge k Sorted Lists
# not two pointer, but heap
class Solution23:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        cnt = count()
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, next(cnt), head))
        cur = dummy = ListNode(-1)

        while len(pq) > 0:
            node = heapq.heappop(pq)[2]
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(pq, (node.next.val, next(cnt), node.next))

        return dummy.next


# 86. Partition List
class Solution86:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = dummy1 = ListNode(-1)
        p2 = dummy2 = ListNode(-1)
        p = head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next


# 876. Middle of the Linked List
class Solution876:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
