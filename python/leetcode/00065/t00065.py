"""
65. Valid Number
Hard
"""

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        m = re.match(r"\s*[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?\s*$", s)
        return bool(m)

    def isNumber1(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False


def test1():
    assert Solution().isNumber(".1") is True


def test2():
    assert Solution().isNumber("0e") is False
