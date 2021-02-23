"""
56. Merge Intervals
Medium


sort
80 ms	16.5 MB
O(n log n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start > result[-1][END]:
                result.append([start, end])
            else:
                result[-1][END] = max(result[-1][END], end)

        return result

