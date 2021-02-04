"""
1254. Number of Closed Islands
Medium
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] != 0:
                return 1

            grid[i][j] = 2
            r = min(
                dfs(i + 1, j),
                dfs(i, j + 1),
                dfs(i - 1, j),
                dfs(i, j - 1),
            )
            return r

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += dfs(i, j)

        return cnt

