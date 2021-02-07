"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium

Runtime: 1004 ms, faster than 50.12% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.
Memory Usage: 37.5 MB, less than 13.35% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.
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
                intervals.append((start, end, end - start + 1))
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
            return not (int1[1] < int2[0] or int2[1] < int1[0])

        # print(len(intervals))
        intervals.sort(key=lambda t: t[2])
        MAX_INT = 10 ** 10
        best_sum = MAX_INT
        for first in range(0, len(intervals) - 1):
            for second in range(first + 1, len(intervals)):
                sum_int = intervals[first][2] + intervals[second][2]
                if sum_int >= best_sum:
                    break
                if not intersect(intervals[first], intervals[second]):
                    best_sum = min(best_sum, sum_int)
        if best_sum == MAX_INT:
            return -1
        return best_sum
