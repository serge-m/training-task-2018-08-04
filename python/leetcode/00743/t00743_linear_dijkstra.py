"""
743. Network Delay Time
Medium

linear search dijkstra

"""

from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: {} for i in range(n)}
        for u, v, w in times:
            adj[u - 1][v - 1] = w

        MAXDIST = 10 ** 10
        min_dist = [MAXDIST for i in range(n)]
        visited = [False for i in range(n)]
        min_dist[k - 1] = 0

        for i in range(n):
            u = find_min(min_dist, visited)
            # print(i, "u=", u, "visited=", visited, "min_dist", min_dist)
            if u is None:
                break
            visited[u] = True
            for v in adj[u]:
                # print("v", v, adj[u][v])
                if not visited[v]:
                    if min_dist[u] + adj[u][v] < min_dist[v]:
                        min_dist[v] = min_dist[u] + adj[u][v]

        max_dist = None
        for i in range(n):
            if min_dist[i] is MAXDIST:
                return -1
            if max_dist is None or min_dist[i] > max_dist:
                max_dist = min_dist[i]
        return max_dist


def find_min(min_dist, visited):
    n = len(min_dist)
    best_u = None
    for u in range(n):
        if not visited[u]:
            if (best_u is None or min_dist[best_u] > min_dist[u]):
                best_u = u
    return best_u
