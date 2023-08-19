class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data=data)
        else:
            current = self.root
            while current.next is not None:
                current = current.next

    def delete(self, index):
        if index == 0:
            if self.root is not None:
                self.root = self.root.next
            else:
                raise IndexError("Index out of range")
        else:
            current: Node = self.root
            for _i in range(index):
                if current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            current.next = None
