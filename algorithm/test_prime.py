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


def is_prime2(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def generate_primes(limit):
    for num in range(2, limit):
        if is_prime2(num):
            yield num


def test_prime_table():
    prime_table = set()
    for prime in generate_primes(100):
        prime_table.add(prime)
    assert prime_table == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
