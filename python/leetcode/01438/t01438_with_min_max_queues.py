"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

two pointers, min/max window
"""
from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        qmax = deque()
        qmin = deque()
        start = 0
        end = 0

        def add_with_condition(q, value, pop_pred):
            while q and pop_pred(q[-1], value):
                q.pop()
            q.append(value)

        def add(value):
            add_with_condition(qmax, value, pop_pred=lambda old, new: old < new)
            add_with_condition(qmin, value, pop_pred=lambda old, new: old > new)

        def delete(value):
            if qmax[0] == value:
                qmax.popleft()
            if qmin[0] == value:
                qmin.popleft()

        while end < n:
            add(nums[end])
            largest = qmax[0]
            smallest = qmin[0]
            if largest - smallest > limit:
                delete(nums[start])
                start += 1
            end += 1
        return end - start

