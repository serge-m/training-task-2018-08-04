"""
973. K Closest Points to Origin
medium

simple solution: sorting the whole array
linear solution with quickselect (hoare partition)
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return self.find(points, 0, len(points) - 1, K)

    def find(self, points, start, end, K):
        if start == end:
            if K <= 1:
                return points[start:start + K]
            else:
                raise ValueError("hmmm")
        mid = self.partition(points, start, end)
        cnt_in_left = mid + 1 - start
        if K < cnt_in_left:
            return self.find(points, start, mid, K)
        elif K > cnt_in_left:
            return points[start:mid + 1] + self.find(points, mid + 1, end, K - cnt_in_left)
        else:
            return points[start:mid + 1]

    def partition(self, points, start, end):
        i_pivot = (start + end) // 2
        pivot = key(points[i_pivot])
        i = start - 1
        j = end + 1
        while True:
            i += 1
            while key(points[i]) < pivot:
                i += 1
            j -= 1
            while pivot < key(points[j]):
                j -= 1
            if i >= j:
                break
            points[i], points[j] = points[j], points[i]

        return j


def key(pt):
    return pt[0] ** 2 + pt[1] ** 2


def test_1():
    sol = Solution()
    assert sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_2():
    sol = Solution()
    assert sorted(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == sorted([[3, 3], [-2, 4]])


def test_3():
    sol = Solution()
    assert sorted(sol.kClosest(
        [[0, 1], [1, 0]], 2
    )) == sorted([[0, 1], [1, 0]])
