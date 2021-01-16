"""
76. Minimum Window Substring
Hard

t = 55

-----------------------------------------------------


.  . .   -- -
ADOBECODEBANC"
0123456789012

A0 B3 C5
5-0 +1= 6
b:9
no better
a:10
10-5+ 1 = 6 - same

update current latest position of the current letter/
find minimum of the all positions
compute new length
if new is better: update the best.

How to compute minimum effectively? Keep some additional info (next best). single linked list?

Q How to deal with duplicates? having a queue for each char.


"""

from collections import deque, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        registry = Registry(t)
        for i, c in enumerate(s):
            registry.add(i, c)
        start, end = registry.best_range
        return s[start: end + 1]


class Registry:
    def __init__(self, t):
        self.target_cnt = len(t)
        self.cnt = 0
        self.positions = defaultdict(deque)

        for c in t:
            self.positions[c].append(None)

        self.chain = Chain()
        self.best_len = None
        self.best_range = (0, -1)

    def add(self, pos, c):
        if c not in self.positions:
            return
        old = self.positions[c].popleft()
        self.chain.remove(old)
        self.positions[c].append(pos)
        self.chain.append(pos)
        if old is None:
            self.cnt += 1
        if self.cnt == self.target_cnt:
            if self.best_len is None or self.chain.len() < self.best_len:
                self.best_len = self.chain.len()
                self.best_range = self.chain.range()


class Chain:
    last = object()
    first = object()

    def __init__(self):
        self.prev = {
            self.last: self.first,
        }
        self.next = {
            self.first: self.last,
        }

    def remove(self, pos):
        if pos is None:
            return
        p = self.prev.pop(pos)
        n = self.next.pop(pos)
        self.next[p] = n
        self.prev[n] = p

    def append(self, pos):
        old_end = self.prev[self.last]
        self.prev[self.last] = pos
        self.next[old_end] = pos
        self.prev[pos] = old_end
        self.next[pos] = self.last

    def len(self):
        return self.prev[self.last] - self.next[self.first] + 1

    def range(self):
        return self.next[self.first], self.prev[self.last]





















