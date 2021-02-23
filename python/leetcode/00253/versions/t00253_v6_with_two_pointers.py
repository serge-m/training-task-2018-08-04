"""
253. Meeting Rooms II
Medium

with two pointers

	72 ms	17.5 MB
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted((seg[0] for seg in intervals))
        ends = sorted((seg[1] for seg in intervals))
        n = len(intervals)
        p_start = 0
        p_end = 0
        cur = 0
        best = 0
        while p_start < n:
            if starts[p_start] < ends[p_end]:
                p_start += 1
                cur += 1
            elif starts[p_start] == ends[p_end]:
                p_start += 1
                p_end += 1
            else:
                p_end += 1
                cur -= 1
            best = max(best, cur)
        return best


"""
0 5 15
10 20 30
"""
