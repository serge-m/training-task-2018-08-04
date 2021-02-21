"""
1756. Design Most Recently Used Queue
Medium
"""

from sortedcontainers import SortedList


class MRUQueue:

    def __init__(self, n: int):
        self.a = SortedList([[i, i] for i in range(1, n + 1)])
        self.last_w = n

    def fetch(self, k: int) -> int:
        i = k - 1
        w, val = self.a.pop(i)
        self.last_w += 1
        self.a.add([self.last_w, val])
        return val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
