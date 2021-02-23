"""
57. Insert Interval
Medium

O(n + log n) including copying
76 ms	17.4 MB
"""

import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        a, b = newInterval
        pa = bisect.bisect_left(intervals, [a, -1])
        pb = bisect.bisect_left(intervals, [b, -1])

        merge_start = pa
        if pa > 0 and intersects(intervals[pa - 1], newInterval):
            merge_start = pa - 1

        merge_end = pb
        if pb < n and intersects(intervals[pb], newInterval):
            merge_end = pb + 1

        if merge_start == merge_end:
            merged = [a, b]
        else:
            merged = [min(intervals[merge_start][0], a), max(intervals[merge_end - 1][1], b)]

        return intervals[:merge_start] + [merged] + intervals[merge_end:]


def intersects(u, v):
    return not (u[1] < v[0] or v[1] < u[0])
