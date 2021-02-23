"""
56. Merge Intervals
Medium


SortedList as a storage for non intersecting intervals.
Works for online processing
	112 ms	16.7 MB
O(n log n)
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        points = SortedList()

        for start, end in intervals:
            i_start = points.bisect_left(start)
            i_end = points.bisect_right(end)
            del points[i_start:i_end]
            if i_start % 2 == 0:
                points.add(start)
            if i_end % 2 == 0:
                points.add(end)

        result = [[points[i], points[i + 1]] for i in range(0, len(points), 2)]
        return result



