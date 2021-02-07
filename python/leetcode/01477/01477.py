"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium

time limit
"""

import itertools
from typing import List, Tuple


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        intervals = []

        csum = list(itertools.accumulate(arr))
        csum.append(0)

        start = 0
        end = 0
        s = 0
        while end < n:

            s = csum[end] - csum[start - 1]
            # print(start, end, "sum", s, intervals)
            if s == target:
                intervals.append((start, end))
                start += 1
                end += 1
            elif s > target:
                start += 1
                end = max(start, end)
            else:  # s < target
                end += 1

        if len(intervals) < 2:
            return -1

        def intersect(int1, int2):
            return int1[1] >= int2[0]

        def size(i: Tuple):
            return i[1] - i[0] + 1

        MAX_INT = 10 ** 10
        best_sum = MAX_INT
        for first in range(0, len(intervals) - 1):
            if size(intervals[first]) >= best_sum:
                continue
            for second in range(first + 1, len(intervals)):
                if not intersect(intervals[first], intervals[second]):
                    sum_int = size(intervals[first]) + size(intervals[second])
                    best_sum = min(best_sum, sum_int)
        if best_sum == MAX_INT:
            return -1
        return best_sum
