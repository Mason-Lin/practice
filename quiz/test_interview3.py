from collections import Counter, deque


def palindromic(s: str) -> str:
    # 沒考慮到 s 是 None 的情況
    try:
        s = str(s)
    except TypeError:
        return ""

    length = len(s)
    counter = Counter(s)

    cnt = 0
    for c in s:
        if c.isalpha() and c.lower() == c:
            cnt += 1
    if cnt != length:  # 當時寫反了
        return ""

    cnt = 0
    odd_char, odd_freq = "", 0  # 當時沒注意到這個變數 unbound 的問題
    if length == 0:
        return ""
    if length % 2:
        for char, freq in counter.items():
            if freq % 2:
                odd_char = char
                odd_freq = freq
                cnt += 1
                if cnt > 1:
                    return ""

    output = deque()
    if cnt == 1:  # 沒有考慮到這個情況, 直接塞進去
        output.append(odd_char * odd_freq)
    for char, freq in counter.items():
        if not freq % 2:
            for _ in range(freq // 2):
                output.append(char)
                output.appendleft(char)
    return "".join(list(output))


def test_palindromic():
    assert palindromic("googlee") == "eoglgoe"
    assert palindromic("glllg") == "glllg"
    assert palindromic("glg") == "glg"
    assert palindromic("") == ""
    assert palindromic("a") == "a"
    assert palindromic("A") == ""
    assert palindromic("b" * 1024) == "b" * 1024
    assert palindromic(None) == ""
