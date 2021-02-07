"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium

sliding separation point, sliding window
with a hint 1
wit binary search

Runtime: 1164 ms, faster than 28.88% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.
Memory Usage: 47.6 MB, less than 5.10% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.

"""

import itertools
from typing import List, Tuple
import bisect


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        intervals = []

        csum = list(itertools.accumulate(arr))
        csum.append(0)

        MAXINT = 10 ** 10

        prefix = []
        suffix = []

        start = 0
        end = 0
        s = 0
        while end < n:

            s = csum[end] - csum[start - 1]
            # print(start, end, "sum", s, intervals)
            if s == target:
                l = end - start + 1
                prefix.append([end + 1, l])
                if len(prefix) > 1:
                    prefix[-1][1] = min(prefix[-2][1], l)
                suffix.append([start, l])
                start += 1
                end += 1
            elif s > target:
                start += 1
                end = max(start, end)
            else:  # s < target
                end += 1

        # print("prefix", prefix)
        # print("suffix", suffix)

        for i in range(len(prefix) - 2, -1, -1):
            suffix[i][1] = min(suffix[i][1], suffix[i + 1][1])
        # print("prefix", prefix)
        # print("suffix", suffix)
        best = MAXINT
        for i in range(0, len(prefix)):
            j = bisect.bisect_right(suffix, [prefix[i][0], 0])
            # print("pre", i, "suf", j)
            if j == len(prefix):
                break
            best = min(best, prefix[i][1] + suffix[j][1])
            # print(best)

        if best == MAXINT:
            return -1
        return best

