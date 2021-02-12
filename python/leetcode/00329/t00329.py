"""
329. Longest Increasing Path in a Matrix
Hard
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        v = [[None for k in range(n)] for i in range(m)]

        # nxt = [[(i, j) for k in range(n)] for i in range(m)]

        def dfs(i, j):
            if v[i][j] is not None:
                return v[i][j]
            v[i][j] = 1
            for (ni, nj) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:  # valid coord and increasing
                    val = dfs(ni, nj)
                    if val + 1 > v[i][j]:  # got longer path
                        v[i][j] = val + 1
                        # nxt[i][j] = (ni, nj)
            return v[i][j]

        best = 0
        for i in range(m):
            for j in range(n):
                best = max(best, dfs(i, j))
        return best
