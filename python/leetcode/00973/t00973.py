"""
973. K Closest Points to Origin
medium
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda pt: pt[0] ** 2 + pt[1] ** 2)
        return points[:K]

