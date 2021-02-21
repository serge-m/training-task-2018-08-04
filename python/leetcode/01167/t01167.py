"""
1167. Minimum Cost to Connect Sticks
Medium

heap
"""

import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        total = 0
        while len(sticks) > 1:
            top = heapq.heappop(sticks)
            prev = heapq.heappop(sticks)
            c = top + prev
            total += c
            heapq.heappush(sticks, c)
        return total
