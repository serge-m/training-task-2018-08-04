"""
690. Employee Importance
Easy

t=7
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = defaultdict(list)  # TODO: no need for that
        imp = {}
        for emp in employees:
            eid, i, nxt = emp.id, emp.importance, emp.subordinates
            imp[eid] = i
            adj[eid].extend(nxt)

        def dfs(eid):
            result = imp.get(eid, 0)
            for nxt in adj[eid]:
                result += dfs(nxt)
            return result

        return dfs(id)
