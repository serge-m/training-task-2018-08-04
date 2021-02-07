"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
"""
# from dataclasses import dataclass
from typing import List

from sortedcontainers import SortedList, SortedDict


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        w = SortedDict()
        start = 0
        end = 0

        def add(value):
            if value not in w:
                w[value] = 0
            w[value] += 1

        def delete(value):
            if w[value] == 1:
                del w[value]
            else:
                w[value] -= 1

        while end < n:

            add(nums[end])
            largest = w.peekitem(index=-1)
            smallest = w.peekitem(index=0)
            if largest[0] - smallest[0] > limit:
                delete(nums[start])
                start += 1
            end += 1
        return end - start

