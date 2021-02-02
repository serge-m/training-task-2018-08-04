"""
295. Find Median from Data Stream
Hard

t=5

"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        if n % 2 == 1:
            return self.array[n // 2]
        else:
            return (self.array[n // 2 - 1] + self.array[n // 2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
