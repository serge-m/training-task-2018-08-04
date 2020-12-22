"""
207. Course Schedule
topological sort, topsort
"""

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = defaultdict(list)

        for (u, v) in prerequisites:
            adj[u].append(v)

        visited = [False for u in range(n)]
        visited_in_cur_pass = [False for u in range(n)]
        result = []

        for u in range(n):
            if not visited[u]:
                if not dfs(u, adj, visited, visited_in_cur_pass, result):
                    return False

        return all(visited)


def dfs(u, adj, visited, visited_in_cur_pass, result):
    visited_in_cur_pass[u] = True
    for v in adj[u]:
        if visited_in_cur_pass[v]:
            return False
        if visited[v]:
            continue
        if not dfs(v, adj, visited, visited_in_cur_pass, result):
            return False
        result.append(v)
    visited_in_cur_pass[u] = False
    visited[u] = True
    return True


def test_1():
    assert Solution().canFinish(2, [[0, 1]]) is True
    assert Solution().canFinish(2, [[1, 0]]) is True


def test_2():
    assert Solution().canFinish(2, [[0, 1], [1, 0]]) is False


def test_3():
    assert Solution().canFinish(3, [[0, 1], [1, 2], [0, 2]]) is True
