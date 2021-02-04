"""
1376. Time Needed to Inform All Employees
Medium


"""

from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ms = manager
        ts = informTime

        distances = [0 for i in range(n)]
        for i in range(n):
            cur = i
            if distances[cur] != 0:
                continue
            d = 0
            while True:
                cur = ms[cur]
                if cur == -1:
                    break
                d += ts[cur]
                if d <= distances[cur]:
                    break
                else:
                    distances[cur] = d
        return distances[headID]


