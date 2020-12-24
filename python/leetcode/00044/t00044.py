from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def is_end(st, i):
            return i == len(st)

        @lru_cache(maxsize=None)
        def match(si, pi):
            # print(s[si:], p[pi:])
            if is_end(p, pi):
                return is_end(s, si)

            c = p[pi]

            if c == '?':
                if is_end(s, si):
                    return False
                return match(si + 1, pi + 1)

            if c == '*':
                for i in range(si, len(s) + 1):
                    if match(i, pi + 1):
                        return True
                return False

            if is_end(s, si):
                return False

            if c != s[si]:
                return False

            return match(si + 1, pi + 1)

        return match(0, 0)
