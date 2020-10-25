import functools


class Solution:
    @functools.lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""

        if p[-1] == ".":
            if s == "":
                return False
            return self.isMatch(s[:-1], p[:-1])

        if p[-1] != "*":  # normal symbol
            if s == "":
                return False
            if s[-1] != p[-1]:
                return False
            return self.isMatch(s[:-1], p[:-1])

        # p[-1] == "*"
        char = p[-2]
        i_s = len(s) - 1
        if self.isMatch(s, p[:-2]):
            return True
        while i_s >= 0 and (char == '.' or s[i_s] == char):
            if self.isMatch(s[:i_s], p[:-2]):
                return True
            i_s -= 1
        return False


def test():
    assert Solution().isMatch("aab", "c*a*b") is True
