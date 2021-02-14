"""
323. Number of Connected Components in an Undirected Graph
Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(u):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)

        cnt_components = 0
        for u in range(n):
            if u not in visited:
                cnt_components += 1
                dfs(u)

        return cnt_components

