"""
295. Find Median from Data Stream
Hard

t = 42
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        lowest_in_large = heapq.heappop(self.large)
        heapq.heappush(self.small, -lowest_in_large)

        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)

    def findMedian(self) -> float:
        n = len(self.small) + len(self.large)
        if n % 2 == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


"""
add 1:
small  []
large  [1] 

add 2:
small  [-1]
large    [2]


median: (1 + 2 ) / 2 = 0.5

add 3
small  [-1]
large    [2, 3]

median 2




"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
