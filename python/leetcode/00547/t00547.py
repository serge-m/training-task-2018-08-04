"""
547. Friend Circles
number of connected components
amazon
"""

from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        circle = [-1 for i in range(n)]
        num_circles = 0
        for i in range(n):
            if circle[i] == -1:
                num_circles += 1
                visit(i, i, circle, M)
        return num_circles


def visit(cur, color, circle, M):
    if circle[cur] != -1:
        return
    circle[cur] = color
    for i in range(len(M)):
        if M[cur][i] == 1:
            visit(i, color, circle, M)
