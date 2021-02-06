"""
528. Random Pick with Weight
Medium

t=45

w[i] > 0
"""
import random
import itertools
from typing import List
import bisect


class Solution:  # binsearch

    def __init__(self, w: List[int]):
        self.random = random.Random(0)
        self.w = w
        self.sum = sum(w)
        self.csum = list(itertools.accumulate(w))
        self.m = len(w)

    def pickIndex(self) -> int:
        pos = self.random.random() * self.sum
        idx = bisect.bisect_left(self.csum, pos)
        return idx


class SolutionSmart:

    def __init__(self, w: List[int]):
        self.random = random.Random(0)
        self.w = w
        self.sum = sum(w)
        self.csum = list(itertools.accumulate(w))
        self.m = len(w)
        self.x = self.random.random() * self.sum / self.m
        self.cur = 0

    def pickIndex(self) -> int:
        # print(self.__dict__)
        while 1:
            if self.cur == self.m:
                self.cur = 0
                self.x = self.random.random() * self.sum / self.m
            if self.csum[self.cur] >= self.x:
                break
            self.cur += 1
        self.x += self.sum / self.m

        return self.cur

# s = Solution([1,3])
# for k in range(8):
#     print(s.pickIndex())
# print("------")
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
