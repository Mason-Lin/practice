"""dict is hash table already."""
import pytest

UNUSED = (None, None)


class HashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = dict.fromkeys(range(size), UNUSED)

    def put(self, key, value):
        for index in self._hash_generator(key):
            if self.table[index] is UNUSED:
                self.table[index] = (key, value)
                return
        raise IndexError("Hash table is full")

    def get(self, key, default=None):
        for index in self._hash_generator(key):
            if self.table[index] is UNUSED:
                continue

            if self.table[index][0] == key:
                return self.table[index][1]

        return default

    def _hash_generator(self, index):
        start = hash(index) % self.size
        yield start
        probe = (5 * hash(index) + 1) % self.size
        while probe != start:
            probe = (5 * probe + 1) % self.size
            yield probe
        raise IndexError("Hash table is full")


def test_all():
    h = HashTable()
    h.put("a", 1)
    h.put("b", 2)
    assert h.get("a") == 1
    assert h.get("b") == 2

    with pytest.raises(IndexError):
        h.put("c", 3)
