def test_all():
    d = {"a": 1, "b": 2, "c": 3}
    d["d"] = 4
    assert d["a"] == 1
    d.update({"a": 2, "b": 3})
    assert d["a"] == 2
    assert list(d.items()) == [("a", 2), ("b", 3), ("c", 3), ("d", 4)]
    assert d.get("a") == 2
    assert d.get("e") is None

    assert d.pop("a") == 2
    assert list(d.items()) == [("b", 3), ("c", 3), ("d", 4)]
