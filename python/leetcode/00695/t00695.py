"""
695. Max Area of Island
Medium

t=6

recursion, dfs

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2  # visited

            size = 1
            for di, dj in moves:
                size += dfs(i + di, j + dj)
            return size

        max_size = 0
        for i in range(m):
            for j in range(n):
                max_size = max(max_size, dfs(i, j))

        return max_size
