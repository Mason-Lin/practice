# Coding: find first occurrence of string in sentence
sentence = "can a cat eat grass cat?"
substr = "cat"


def find_str(sentence, substr):
    target = sum(hash(c) for c in substr)
    curr = sum(hash(c) for c in sentence[: len(substr)])

    i, j = 0, len(substr)
    curr += hash(sentence[i])
    curr -= hash(sentence[j])
    while j < len(sentence):
        curr -= hash(sentence[i])
        curr += hash(sentence[j])
        if curr == target:
            return i
        i += 1
        j += 1
    return -1


assert find_str(sentence, substr) == 6
