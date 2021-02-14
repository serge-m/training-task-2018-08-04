"""
743. Network Delay Time
Medium

O(n^3)
floyd algorithm

Runtime: 1296 ms
Memory Usage: 16 MB
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10 ** 10
        d = init_d(n, INF, times)
        # print(d)
        floyd(n, d)
        k -= 1
        # print(d)
        for i in range(n):
            if d[k][i] is INF:
                return -1

        return max(d[k][i] for i in range(n) if i != k)


def floyd(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                candidate = d[i][k] + d[k][j]
                if d[i][j] > candidate:
                    d[i][j] = candidate


def init_d(n, inf, times):
    d = [
        [inf for j in range(n)]
        for i in range(n)
    ]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in times:
        d[u - 1][v - 1] = w
    return d




