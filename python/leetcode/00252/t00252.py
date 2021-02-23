"""
252. Meeting Rooms
Easy

A strange solution.
Maintaining non-intersecting intervals in SortedDict.
when an interval starts we set sd[star] = 1
when an interval ends we set sd[end] = -1
for each incoming interval we are checking if it falls into some other interval

O(n log n)
152 ms	17.8 MB
"""

from sortedcontainers import SortedDict
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        points = SortedDict()
        for start, end in intervals:
            # print(start, end)
            # print(points)
            i_start = points.bisect_right(start)
            i_end = points.bisect_left(end)
            # print("i_start", i_start)
            # print("i_end", i_end)
            if i_end != i_start:
                return False
            if i_start > 0 and points.peekitem(i_start-1)[1] == 1:
                return False

            if points.get(start) == -1:
                del points[start]
            else:
                points[start] = 1

            if points.get(end) == 1:
                del points[end]
            else:
                points[end] = -1
        return True

