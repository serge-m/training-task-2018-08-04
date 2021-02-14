"""
332. Reconstruct Itinerary
Medium

"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        e = len(tickets)
        tickets.sort()
        adj = defaultdict(lambda: defaultdict(int))
        for u, v in tickets:
            adj[u][v] += 1

        seq = []

        def dfs(u):
            nonlocal seq
            if len(seq) == e + 1:
                return seq
            for v in adj[u]:
                if adj[u][v] > 0:
                    adj[u][v] -= 1
                    seq.append(v)
                    r = dfs(v)
                    if r is not None:
                        return r
                    seq.pop()
                    adj[u][v] += 1
            return None

        seq.append("JFK")
        return dfs("JFK")



