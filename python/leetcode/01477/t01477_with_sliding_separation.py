"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium

sliding separation point, sliding window
with a hint 1

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

        MAXINT = 10 ** 10

        prefix = [MAXINT for i in range(n + 1)]
        suffix = [MAXINT for i in range(n + 1)]

        for start, end, l in intervals:
            prefix[end + 1] = l
            suffix[start] = l

        for i in range(1, n):
            prefix[i] = min(prefix[i], prefix[i - 1])
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])

        best = MAXINT
        for i in range(0, n):
            best = min(best, suffix[i] + prefix[i])
        if best == MAXINT:
            return -1
        return best

