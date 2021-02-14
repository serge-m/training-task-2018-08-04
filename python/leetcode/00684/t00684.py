"""
684. Redundant Connection
Medium

"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DSet()
        for u, v in edges:
            if ds.union(u, v) == 0:
                return [u, v]
        return None


class DSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, a):
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 1

    def union(self, a, b):
        self.add(a)
        self.add(b)

        pa = self.parent[a] = self.find(a)
        pb = self.parent[b] = self.find(b)

        if pa == pb:
            return 0

        # we want b to  have larger rank

        if self.rank[pa] > self.rank[pb]:
            pa, pb = pb, pa

        if self.rank[pb] == self.rank[pa]:
            self.rank[pb] += 1

        self.parent[pa] = pb
        return 1

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

