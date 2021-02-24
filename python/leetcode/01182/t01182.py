"""
1182. Shortest Distance to Target Color
Medium


2000 ms	38 MB
"""

from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        INF = 10 ** 6
        nearest_dist = [None, [INF] * n, [INF] * n, [INF] * n]
        for i in range(n):
            c = colors[i]
            for from_c in [1, 2, 3]:
                nearest_cur_c = nearest_dist[from_c]
                if c == from_c:
                    nearest_cur_c[i] = 0
                else:
                    if i > 0 and nearest_cur_c[i - 1] != INF:
                        nearest_cur_c[i] = nearest_cur_c[i - 1] + 1
                    else:
                        pass

        for i in range(n - 1, -1, -1):
            c = colors[i]
            for from_c in [1, 2, 3]:
                nearest_cur_c = nearest_dist[from_c]
                if c == from_c:
                    nearest_cur_c[i] = 0
                else:
                    if i < n - 1 and nearest_cur_c[i + 1] != INF:
                        nearest_cur_c[i] = min(nearest_cur_c[i], nearest_cur_c[i + 1] + 1)
                    else:
                        pass

        return [
            nearest_dist[c][i] if nearest_dist[c][i] != INF else -1
            for i, c in queries
        ]
