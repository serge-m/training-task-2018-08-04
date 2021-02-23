"""
253. Meeting Rooms II
Medium

with SortedDict

100 ms	18.1 MB
"""
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = SortedDict()

        for start, end in intervals:
            points[start] = points.get(start, 0) + 1
            points[end] = points.get(end, 0) - 1

        best = 0
        cur = 0
        for v in points.values():
            cur += v
            best = max(best, cur)
        return best
