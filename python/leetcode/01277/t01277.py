"""
1277. Count Square Submatrices with All Ones
Medium

t=5

dynamic programming
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1

        s = 0
        for i in range(0, m):
            for j in range(0, n):
                s += matrix[i][j]

        return s


