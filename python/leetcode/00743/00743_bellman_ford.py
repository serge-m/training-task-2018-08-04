"""
743. Network Delay Time
Medium

O(V*E)
bellman ford

Runtime: 1124 ms
Memory Usage: 16 MB
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10 ** 10
        d = [INF for i in range(n)]
        d[k - 1] = 0

        bellman_ford_wo_loops(n, d, times)

        for i in range(n):
            if d[i] is INF:
                return -1

        return max(d[i] for i in range(n))


def bellman_ford_wo_loops(n, d, times):
    for it in range(n - 1):
        for u, v, w in times:
            c = d[u - 1] + w
            if d[v - 1] > c:
                d[v - 1] = c






