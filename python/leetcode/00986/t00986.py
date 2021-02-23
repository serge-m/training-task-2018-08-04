"""
986. Interval List Intersections
Medium

156 ms	15.3 MB

"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a, b = firstList, secondList
        if len(a) == 0 or len(b) == 0:
            return []

        na = len(a)
        nb = len(b)
        ia = 0
        ib = 0

        def do_step():
            nonlocal ia, ib
            if a[ia][1] < b[ib][1]:
                ia += 1
            else:
                ib += 1

        result = []
        while ia < na and ib < nb:
            inter = intersect(a[ia], b[ib])
            if inter is not None:
                result.append(inter)
            do_step()

        return result


def intersect(u, v):
    start, end = max(u[0], v[0]), min(u[1], v[1])
    if start > end:
        return None
    return [start, end]
