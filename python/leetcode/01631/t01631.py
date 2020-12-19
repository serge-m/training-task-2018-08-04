import heapq
from typing import List
import sys

inf = sys.maxsize
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, columns = len(heights), len(heights[0])  # assuming input is correct
        visited = [[0 for i in row] for row in heights]
        best = [[inf for i in row] for row in heights]
        best[0][0] = 0
        q = [(best[0][0], (0, 0))]

        while q:
            (_, (y, x)) = heapq.heappop(q)
            if (y, x) == (rows - 1, columns - 1):
                return best[y][x]
            if visited[y][x]:
                continue
            for (dy, dx) in moves:
                ny = y + dy
                nx = x + dx
                if not (0 <= nx < columns and 0 <= ny < rows):
                    continue
                nh = heights[ny][nx]
                nsum = max(best[y][x], abs(heights[y][x] - nh))
                if nsum < best[ny][nx]:
                    best[ny][nx] = nsum
                    heapq.heappush(q, (nsum, (ny, nx)))
            visited[y][x] = True

        assert False, "should not be here"



def test_1():
    assert Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) == 2
