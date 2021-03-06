"""
752. Open the Lock

t = 50

"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(map(int, deadends))
        target = int(target)
        start = 0
        q = deque()

        if target not in visited:
            q.append((0, target))

        while True:
            try:
                (distance, state) = q.popleft()
            except IndexError:
                return -1

            if state == start:
                return distance

            for nxt in neighbors(state):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((distance + 1, nxt))


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


def test_solution():
    assert Solution().openLock(["0000"], "8888") == -1


def test_solution2():
    assert Solution().openLock([], "8888") == 2*4
