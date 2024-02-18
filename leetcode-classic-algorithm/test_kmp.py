# Python program for KMP Algorithm
# None of one can be run, didn't find a template for KMP algorithm yet
# BUG
# BUG
# BUG
# BUG
# BUG
# BUG


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index", str(i - j))
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    length = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
# assert KMPSearch(pat, txt) == 10


def kmp(s: str, t: str) -> int:
    n = len(s)
    dp = [0] * n
    v = 0
    for i in range(1, n):
        while v and s[i] != t[v]:
            v = dp[v - 1]
        v = dp[i] = v + (s[i] == t[v])


def fail_test_kmp_func():
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    assert kmp(txt, pat) == 10

    txt = "abcxabcdabxabcdabcdabc"
    pat = "abcdabc"
    assert kmp(txt, pat) == 11
