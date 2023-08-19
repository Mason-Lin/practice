from collections import defaultdict


def test_all():
    hash_table = defaultdict(list)
    hash_table[hash("a")].append(1)
    for value in hash_table[hash("a")]:
        if value == 1:
            break
    else:
        raise ValueError("Value not found")

    hash_table[hash("b")].append(2)
    assert hash("b") in hash_table
