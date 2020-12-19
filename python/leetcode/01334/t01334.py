from collections import defaultdict
import sys
from typing import List

inf = sys.maxsize


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        best = [[inf for i in range(n)]
                for j in range(n)]

        adj = defaultdict(defaultdict)
        for (u, v, w) in edges:
            adj[u][v] = adj[v][u] = w
            best[u][v] = best[v][u] = w

        for u in range(0, n):
            adj[u][u] = 0
            best[u][u] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if best[i][k] + best[k][j] < best[i][j]:
                        best[i][j] = best[j][i] = best[i][k] + best[k][j]

        smallest_c = inf
        best_city = -1
        for u in range(n):
            c = 0
            for v in range(n):
                if best[u][v] <= distanceThreshold:
                    c += 1
            if c <= smallest_c:
                smallest_c = c
                best_city = u
        return best_city
