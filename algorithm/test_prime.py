def is_prime(x):
    t = 2
    while t * t <= x:
        if x % t == 0:
            return False
        t += 1
    return True


def test_is_prime():
    assert is_prime(19) is True
    assert is_prime(91) is False
