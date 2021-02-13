"""
310. Minimum Height Trees
Medium

"""

from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        q = []
        for u in range(n):
            if len(adj[u]) == 1:
                q.append(u)

        while q:
            prev_q = q
            q = []
            for u in prev_q:
                for v in adj[u]:
                    adj[v].remove(u)
                    if len(adj[v]) == 1:
                        q.append(v)
                adj[u].clear()
            if len(q) == 0:
                return prev_q
        return [0]




