"""
221. Maximal Square
Medium

"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = [
            [0 for j in range(n + 1)]
            for i in range(m + 1)
        ]

        best = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    result[i][j] = 0
                else:
                    r = min(result[i - 1][j - 1], result[i][j - 1], result[i - 1][j]) + 1
                    result[i][j] = r
                    best = max(best, r)

        #         for l in result:
        #             print(" ".join(map(str,l)))

        return best ** 2


"""
0 1 
1 0

0 0 1 1
0 0 1 1 
0 1 1 1
0 1 1 1
1 1 1 1

"""
