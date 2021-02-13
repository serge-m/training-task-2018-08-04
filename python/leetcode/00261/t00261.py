"""
261. Graph Valid Tree
Medium
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return len(edges) == 0
        adj = {}
        for u, v in edges:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)

        visited = set()

        def dfs(u, prev):
            visited.add(u)
            for v in adj.get(u, []):
                if v == prev:
                    continue
                if v in visited:
                    return False
                if not dfs(v, prev=u):
                    return False
            return True

        if not dfs(0, None):
            return False

        print(visited)
        for i in range(1, n):
            if i not in visited:
                return False

        return True
