def test_all():
    l = [1, 2, 3, 4, 5]
    assert l[0] == 1
    assert l[1] == 2
    assert l[-1] == 5

    assert len(l) == 5
    assert l.pop() == 5
    assert len(l) == 4
    l.append(5)
    assert len(l) == 5

    l.extend([6, 7])
    assert len(l) == 7

    # l == [1, 2, 3, 4, 5, 6, 7]
    l.remove(7)
    # l == [1, 2, 3, 4, 5, 6]
    assert len(l) == 6
    assert l[-1] == 6

    l.insert(0, 0)
    assert l[0] == 0

    assert l.reverse() is None
    assert l[0] == 6
