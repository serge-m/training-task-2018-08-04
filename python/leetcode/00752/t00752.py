"""
start 1133
"""

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque()
        q.append(("0000", 0))
        while True:
            try:
                (state, distance) = q.popleft()
            except IndexError:
                return -1

            if state == target:
                return distance

            visited.add(state)

            for nxt in neighbors(state):
                if nxt not in visited:
                    q.append((nxt, distance + 1))


@lru_cache(maxsize=None)
def next_char(c):
    ci = ord(c) - ord('0')
    n = (ci + 1) % 10
    return chr(n + ord('0'))


@lru_cache(maxsize=None)
def prev_char(c):
    ci = ord(c) - ord('0')
    n = (ci - 1) % 10
    return chr(n + ord('0'))


def neighbors(state):
    return (
        state[0:3] + next_char(state[3]),
        state[0:3] + prev_char(state[3]),
        state[0:2] + next_char(state[2]) + state[3],
        state[0:2] + prev_char(state[2]) + state[3],
        state[0] + next_char(state[1]) + state[2:],
        state[0] + prev_char(state[1]) + state[2:],
        next_char(state[0]) + state[1:],
        prev_char(state[0]) + state[1:]
    )
