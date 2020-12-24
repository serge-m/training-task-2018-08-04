from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return match(s, p)


@lru_cache(maxsize=None)
def match(s, p):
    if p == "":
        if s == "":
            return True
        else:
            return False
    c = p[0]

    if c == '?':
        if s == "":
            return False
        return match(s[1:], p[1:])

    if c == '*':
        for i in range(0, len(s) + 1):
            if match(s[i:], p[1:]):
                return True
        return False

    if s == "":
        return False

    if c != s[0]:
        return False

    return match(s[1:], p[1:])

