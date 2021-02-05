"""
305. Number of Islands II
Hard

"""
from typing import List


class DS:
    def __init__(self):
        self.p = {}
        self.r = {}

    def add(self, x):
        if x in self.p:
            return
        self.p[x] = x
        self.r[x] = 1

    def find(self, x):
        while x != self.p[x]:
            x, self.p[x] = self.p[x], self.p[self.p[x]]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.r[x] > self.r[y]:
            x, y = y, x
        elif self.r[x] == self.r[y]:
            self.r[y] += 1
        self.p[x] = y
        return -1

    def __repr__(self):
        return f"DS({self.p})"


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        land = [
            [0 for i in range(n)]
            for j in range(m)
        ]
        result = []
        ds = DS()
        cnt = 0
        for y, x in positions:
            # print("pos", y, x)
            # print(land)
            if land[y][x] == 0:
                land[y][x] = 1
                cnt += 1
                ds.add((y, x))
                for ny, nx in [
                    (y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)
                ]:

                    if 0 <= nx < n and 0 <= ny < m and land[ny][nx] == 1:
                        # print(ny, nx, ds)
                        cnt += ds.union((y, x), (ny, nx))

            result.append(cnt)
        return result


