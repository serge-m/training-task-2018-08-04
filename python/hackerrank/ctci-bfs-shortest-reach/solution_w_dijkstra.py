# you don't really need Dijkstra here
#
from collections import defaultdict
import heapq
import sys


class Graph:
    inf = sys.maxsize

    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(defaultdict)

    def connect(self, u, v):
        self.adj[u][v] = self.adj[v][u] = 6

    def find_all_distances(self, start):
        best = [self.inf for i in range(self.n)]
        best[start] = 0
        visited = [0 for i in range(self.n)]
        q = [(best[start], start)]
        while q:
            (_, u) = heapq.heappop(q)
            if visited[u]:
                continue
            for v, w in self.adj[u].items():
                if best[u] + w < best[v]:
                    best[v] = best[u] + w
                    heapq.heappush(q, (best[v], v))
            visited[u] = 1

        result = [
            b if b != self.inf else -1
            for u, b in enumerate(best)
            if u != start
        ]
        return result


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    dists = graph.find_all_distances(s - 1)
    print(' '.join(map(str, dists)))
