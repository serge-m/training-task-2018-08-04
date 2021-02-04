"""
1376. Time Needed to Inform All Employees
Medium


"""

from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ms = manager
        ts = informTime

        adj = defaultdict(dict)
        for i, (m, t) in enumerate(zip(ms, ts)):
            if m != -1:
                adj[m][i] = ts[m]

        def dfs(cur, t):
            result = t
            for nxt, dt in adj[cur].items():
                result = max(result, dfs(nxt, t + dt))
            return result

        return dfs(headID, 0)
