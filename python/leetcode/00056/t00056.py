"""
56. Merge Intervals
Medium

t=11
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[1])
        if not intervals:
            return []
        r = []
        for cur in intervals:
            r.append(cur)
            while len(r) >= 2 and intersecting(r[-2], r[-1]):
                r.append(merge(r.pop(), r.pop()))

        return r


def intersecting(int1, int2):
    return int1[1] >= int2[0]


def merge(int1: List[int], int2: List[int]) -> List[int]:
    return [min(int1[0], int2[0]), max(int1[1], int2[1])]








