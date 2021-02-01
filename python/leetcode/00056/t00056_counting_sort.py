"""
56. Merge Intervals
Medium

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        min_val = 0
        max_val = 10 ** 4
        starts = [0 for x in range(min_val, max_val + 1)]
        ends = [0 for x in range(min_val, max_val + 1)]
        for start, end in intervals:
            starts[start] += 1
            ends[end] += 1

        result = []
        cur = 0
        prev_start = None
        for x in range(min_val, max_val + 1):
            new_cur = cur - ends[x] + starts[x]
            if cur > 0 and new_cur == 0:
                result.append([prev_start, x])
            elif cur == 0 and new_cur > 0:
                prev_start = x
            elif cur == 0 and starts[x] == ends[x] and starts[x] > 0:
                result.append([x, x])
            cur = new_cur

        return result








