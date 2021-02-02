"""
253. Meeting Rooms II
Medium


version 2
"""

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        max_size = 0
        heap = []
        for start, end in intervals:
            while heap and heap[0] <= start:
                _ = heapq.heappop(heap)
            heapq.heappush(heap, end)
            max_size = max(max_size, len(heap))
        return max_size

"""
0 30
5 10
15 20

0 30
heap 30
maxsize = 1

5 10
heap 10 30
maxsize = 2

15 20
heap 30
heap 20 30
maxsize = 2




"""


"""
0 0
30 1
5 0 
10 1
15 0
20 1

0 0    1
5 0    2
10 1   1 
15 0   2 
20 1   1 
30 1   0






"""

