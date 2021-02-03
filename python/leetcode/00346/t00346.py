"""
346. Moving Average from Data Stream
Easy

t=3

"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.cnt = 0
        self.sum = 0
        self.size = size
        self.buf = deque()


    def next(self, val: int) -> float:
        self.buf.append(val)
        self.sum += val
        self.cnt += 1
        if self.cnt > self.size:
            d = self.buf.popleft()
            self.sum -= d
            self.cnt -=1
        return self.sum / self.cnt



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
