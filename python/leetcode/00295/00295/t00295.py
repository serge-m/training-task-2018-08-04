"""
295. Find Median from Data Stream
Hard

t = 27
s = 2245

"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        self.lo, self.hi = 0, 100
        self.counts = [0 for i in range(self.lo, self.hi+1)]
        self.cnt_mid = 0
        self.cnt_lo = self.cnt_hi = 0


    def addNum(self, num: int) -> None:
        if num < self.lo:
            self.small.append(num)
            self.cnt_lo += 1
            return
        if num > self.hi:
            self.large.append(num)
            self.cnt_hi += 1
            return

        self.counts[num] += 1
        self.cnt_mid +=1


    def findMedian(self) -> float:
        self.small.sort()
        self.large.sort()
        n = self.cnt_lo+self.cnt_mid+self.cnt_hi
        if n % 2 == 1:
            return self._get_idx(n//2)
        else:
            return (self._get_idx(n//2-1) + self._get_idx(n//2)) / 2

    def _get_idx(self, idx):
        if idx < self.cnt_lo:
            return self.small[idx]
        if idx < self.cnt_lo+self.cnt_mid:
            return self._get_mid_idx(idx-self.cnt_lo)
        return self.large[idx - self.cnt_lo - self.cnt_mid]


    def _get_mid_idx(self, idx):
        idx += 1
        s = 0
        for i in range(self.lo, self.hi+1):
            s += self.counts[i]
            if s >= idx:
                return i
        raise RuntimeError("something went wrong")


"""
add 1:
small  []
mid    [0: 0, 1:1 ....]
large

add 2:
small  []
mid    [0: 0, 1:1, 2:2 ....]
large

median:
0 2 0

"""


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
