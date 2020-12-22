"""
547. Friend Circles
number of connected components
amazon
"""

from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0 for i in range(n)]
        num_circles = 0
        for i in range(n):
            if not visited[i]:
                num_circles += 1
                visit(i, visited, M)
        return num_circles


def visit(cur, visited, M):
    visited[cur] = True
    for i in range(len(M)):
        if M[cur][i] == 1 and not visited[i]:
            visit(i, visited, M)
