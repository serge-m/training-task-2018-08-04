"""
743. Network Delay Time
Medium

dijkstra with lazy heap

t=14
d=20201219
"""

import heapq
from collections import defaultdict
import sys

inf = sys.maxsize


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        adj = defaultdict(defaultdict)
        for (u, v, w) in times:
            adj[u][v] = w
        best = {
            u: (inf if u != K else 0)
            for u in range(1, N + 1)
        }
        visited = {
            u: False
            for u in range(1, N + 1)
        }
        q = [(0, K)]
        while q:
            (_, u) = heapq.heappop(q)
            if visited[u]:
                continue
            for v, w in adj[u].items():
                if best[u] + w < best[v]:
                    best[v] = best[u] + w
                    heapq.heappush(q, (best[v], v))
            visited[u] = True

        result = max(best.values())
        if result == inf:
            return -1
        return result
