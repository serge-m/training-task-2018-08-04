"""
start 1133
"""

from collections import deque
import heapq
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(map(int, deadends))
        target = int(target)
        start = 0
        q = [(0, distance_estimation(target), target)]

        while True:
            try:
                (distance, _, state) = heapq.heappop(q)
            except IndexError:
                return -1

            if state == start:
                return distance

            visited.add(state)

            for nxt in neighbors(state):
                if nxt not in visited:
                    heapq.heappush(q, (distance + 1, distance_estimation(nxt), nxt))

            print(len(q))



def distance_estimation(state):
    est = 0
    for i in range(4):
        m = (10 ** i)
        d = state // m % 10
        est += min(d, 10 - d)
    return est


def neighbors(state):
    for i in range(4):
        m = (10 ** i)
        d = state // m % 10
        yield state + (-d + (d + 1) % 10) * m
        yield state + (-d + (d - 1) % 10) * m


def test_ne():
    assert sorted(neighbors(0)) == sorted([
        1000,
        9000,
        100,
        900,
        10,
        90,
        1,
        9
    ])

def test_ne2():
    assert sorted(neighbors(1234)) == sorted([
        2234,
        234,

        1334,
        1134,

        1244,
        1224,

        1235,
        1233,

    ])



if __name__ == '__main__':
    assert Solution().openLock(["0000"], "8888") == -1
