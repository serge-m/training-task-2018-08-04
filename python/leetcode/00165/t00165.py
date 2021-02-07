"""
165. Compare Version Numbers
Medium

"""

import itertools


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def split(s):
            for x in s.split('.'):
                yield (int(x))

        for p1, p2 in itertools.zip_longest(split(version1), split(version2), fillvalue=0):
            if p1 > p2:
                return 1
            elif p1 < p2:
                return -1
        return 0
