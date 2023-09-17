# https://medium.com/@derekfan/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95-template-binary-tree-divide-conquer-75e5f80f2d21
from typing import Optional


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Optional[Node] = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete(self):
        if self.head is None:
            return print("This list is empty")

        if len(self) == 1:
            self.head = None
            return None

        current_node = self.head
        while current_node.next is not None:
            self.tail = current_node
            current_node = current_node.next
        self.tail.next = None
        return None

    def insert(self, index, data):
        """To insert the data to the specific index."""
        if self.head is None:
            raise ValueError("empty list")

        if not 1 <= index <= len(self):
            raise ValueError("index out of range")

        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            cur_idx = 1
            new_node = Node(data)
            current_node = self.head
            while cur_idx + 1 != index:
                current_node = current_node.next
                cur_idx += 1
            new_node.next = current_node.next
            current_node.next = new_node

    def delete_node_by_index(self, index):
        """To delete the specific node."""
        if self.head is None:
            raise ValueError("it's an empty list")

        if index == 1 and len(self) > 1:
            self.head = self.head.next

        elif index == 1 and len(self) == 1:
            self.head = None
            self.tail = None

        elif 1 < index < len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = current_node.next

        elif index == len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = None
            self.tail = previous_node

        else:
            raise ValueError("index out of range")

    def reverse(self):
        previous_node = None
        current_node = self.head
        self.tail = current_node
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = previous_node
        self.head = current_node

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length


# 使用快慢指針找出中點
def findMiddle(node):
    fast = slow = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# 反轉linked list
def reverseNode(node):
    if not node or not node.next:
        return node
    prev = None
    cur = node
    while cur:
        temp = cur
        cur = cur.next
        temp.next = prev
        prev = temp
    return prev
