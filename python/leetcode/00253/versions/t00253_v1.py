"""
253. Meeting Rooms II
Medium

80 ms	17.4 MB
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = [(seg[1], -1) for seg in intervals] + [(seg[0], 1) for seg in intervals]
        points.sort()
        cur = 0
        best = 0
        for p, action in points:
            cur += action
            best = max(best, cur)
        return best
