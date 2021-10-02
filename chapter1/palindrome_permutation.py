from typing import Counter


def palindrome_permutation(s):
    counts = Counter(s)
    count = 0
    for v in counts.values():
        if v % 2:
            if count > 0:
                return False
            else:
                count += 1
    return True