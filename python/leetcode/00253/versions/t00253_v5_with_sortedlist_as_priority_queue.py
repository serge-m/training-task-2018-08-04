"""
253. Meeting Rooms II
Medium

with SortedList as priority queue
100 ms	17.8 MB
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        q = SortedList()

        best = 0
        for start, end in intervals:
            while q and q[0] <= start:
                q.pop(0)
            num_intersects = len(q)
            best = max(best, num_intersects + 1)
            q.add(end)
        return best

