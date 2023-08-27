# Coding: find first occurrence of string in sentence


class Solution:
    def find_str_rabin_karp(self, sentence: str, substr: str) -> int:
        # Following program is the python implementation of
        # Rabin Karp Algorithm given in CLRS book

        # d is the number of characters in the input alphabet
        char_size = 256

        prime = 101  # A prime number

        substr_size = len(substr)
        sentence_size = len(sentence)
        i = 0
        j = 0
        hashed_substr = 0  # hash value for pattern
        hashed_sentence = 0  # hash value for sentence
        h = 1

        # The value of h would be "pow(d, M-1)% q"
        for i in range(substr_size - 1):
            h = (h * char_size) % prime

        # Calculate the hash value of pattern and first window
        # of text
        for i in range(substr_size):
            hashed_substr = (char_size * hashed_substr + ord(substr[i])) % prime
            hashed_sentence = (char_size * hashed_sentence + ord(sentence[i])) % prime

        # Slide the pattern over text one by one
        for i in range(sentence_size - substr_size + 1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters one by one
            if hashed_substr == hashed_sentence:
                # Check for characters one by one
                for j in range(substr_size):
                    if sentence[i + j] != substr[j]:
                        break

                # if p == t and substr[0...M-1] = sentence[i, i + 1, ...i + M-1]
                if j + 1 == substr_size:
                    print(f"Pattern found at index {i}")
                    return i

            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < sentence_size - substr_size:
                hashed_sentence = (char_size * (hashed_sentence - ord(sentence[i]) * h) + ord(sentence[i + substr_size])) % prime

                # We might get negative values of t, converting it to
                # positive
                if hashed_sentence < 0:
                    hashed_sentence = hashed_sentence + prime
        return -1

    # This code is contributed by Bhavya Jain

    def find_str(self, sentence: str, substr: str) -> int:
        target = sum(ord(c) for c in substr)
        curr = sum(ord(c) for c in sentence[: len(substr)])

        i, j = 0, len(substr)
        curr += ord(sentence[i])
        curr -= ord(sentence[j])
        while j < len(sentence):
            curr -= ord(sentence[i])
            curr += ord(sentence[j])
            if curr == target:
                return i
            i += 1
            j += 1
        return -1


def test_it():
    sentence = "can a cat eat grass cat?"
    substr = "cat"

    assert Solution().find_str_rabin_karp(sentence, substr) == 6
    assert Solution().find_str(sentence, substr) == 6
