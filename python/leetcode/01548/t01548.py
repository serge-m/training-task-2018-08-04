"""
1548. The Most Similar Path in a Graph
Hard

"""

from collections import defaultdict


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:

        tp = targetPath
        m = len(tp)
        dp = [[] for i in range(m + 1)]
        prev = [[] for i in range(m + 1)]
        # dp[i][j] - best cost (edit distance) for path tp[0:i] ending at vertex j
        # print("tp", tp)

        adj = defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        # len == 0
        dp[0] = [0 for u in range(n)]
        prev[0] = [None for u in range(n)]
        MAXINT = 2 ** 10

        # len > 0
        for i in range(1, m + 1):
            dp[i] = [None for u in range(n)]
            prev[i] = [None for u in range(n)]
            for u in range(n):
                if tp[i - 1] != names[u]:
                    cost_v = 1
                else:
                    cost_v = 0

                # no need to increase cost
                dp[i][u] = MAXINT
                for v in adj[u]:
                    if dp[i][u] > dp[i - 1][v] + cost_v:
                        dp[i][u] = dp[i - 1][v] + cost_v
                        if i > 1:
                            prev[i][u] = v
            # print("after i ", i)
            # print(dp)
            # print(prev)
        best_cost = None
        best_end = None
        for i, cost in enumerate(dp[m]):
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_end = i

        result = []

        cur = best_end
        for i in range(m, 0, -1):
            result.append(cur)
            cur = prev[i][cur]

        return result[::-1]



