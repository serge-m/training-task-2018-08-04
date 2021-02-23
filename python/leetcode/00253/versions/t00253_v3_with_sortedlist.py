"""
253. Meeting Rooms II
Medium

with SortedList

96 ms	17.7 MB
"""
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ends = SortedList()
        best = 0
        for start, end in intervals:
            pos = ends.bisect_right(start)
            num_intersects = len(ends) - pos
            best = max(best, num_intersects + 1)
            ends.add(end)
        return best

