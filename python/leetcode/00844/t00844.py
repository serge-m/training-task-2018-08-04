"""
844. Backspace String Compare
Easy

t= 5

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def clear(s):
            res = []
            for c in s:
                if c == '#':
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return res
        return clear(S) == clear(T)
