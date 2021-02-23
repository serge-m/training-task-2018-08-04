"""
253. Meeting Rooms II
Medium

with heap
88 ms	17.3 MB

"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        q = []
        best = 0
        for start, end in intervals:
            while q and q[0] <= start:
                heapq.heappop(q)
            num_intersects = len(q)
            best = max(best, num_intersects + 1)
            heapq.heappush(q, end)
        return best

