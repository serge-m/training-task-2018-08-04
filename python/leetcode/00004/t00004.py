from typing import List
from dataclasses import dataclass
from bisect import bisect_left


@dataclass
class Target:
    idx: int
    residual: int

    def with_shift_idx(self, shift):
        return Target(self.idx + shift, self.residual)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_len = len(nums1) + len(nums2)
        return find(nums1, nums2, Target(sum_len // 2, (sum_len + 1) % 2))


def index(lst, target: Target):
    if target.residual == 0:
        return lst[target.idx]
    return (lst[target.idx] + lst[target.idx + 1]) / 2


"""
0 -> None
1 -> 0
2 -> 0, 1
3 -> 1
4 -> 1, 2
5 -> 2 
"""


def find(a: List, b: List, target: Target):
    if len(a) > len(b):
        a, b = b, a

    if len(a) == 0:
        return index(b, target)

    if len(a) == 1:
        pos = bisect_left(b, a[0])
        if target.residual == 1:
            if target.idx == pos or target.idx == pos - 1:
                return (a[0] + b[target.idx]) / 2
            if target.idx < pos:
                return index(b, target)
            return index(b, target.with_shift_idx(-1))
        else:
            if target.idx == pos:
                return a[0]
            if target.idx < pos:
                return index(b, target)
            return index(b, target.with_shift_idx(-1))

    # len(a) and len(b) are at least 2:
    """
    a: 1, 3, 5
    b:      4, 6, 8, 10
    target: 2
    """
    la = len(a)
    lb = len(b)
    ima = la // 2
    imb = lb // 2
    ma = a[ima]
    mb = b[imb]
    pos_mb_in_a = bisect_left(a, mb)
    count_le_mb = imb + pos_mb_in_a
    if target.idx < count_le_mb:
        return find(a[:pos_mb_in_a + 1], b[:imb + 1], target)
    return find(a[pos_mb_in_a:], b[imb:], target.with_shift_idx(-count_le_mb))


def test_find_complex_1():
    assert 5 == find([1, 3, 5], [0, 6, 8, 9], Target(3, 0))
    assert 5 == find([0, 6, 8, 9], [1, 3, 5], Target(3, 0))


def test_find_complex_2():
    assert 5.5 == find([1, 3, 5], [0, 6, 8, 9], Target(3, 1))
    assert 5.5 == find([0, 6, 8, 9], [1, 3, 5], Target(3, 1))


def test_find_complex_3():
    assert 5.5 == find([1, 3, 5], [4, 6, 8, 9], Target(3, 1))
    assert 5.5 == find([4, 6, 8, 9], [1, 3, 5], Target(3, 1))
    assert 5 == find([1, 3, 5], [4, 6, 8, 9], Target(3, 0))
    assert 5 == find([4, 6, 8, 9], [1, 3, 5], Target(3, 0))

def test_find_complex_4():
    assert 4 == find([1, 3, 5], [4, 6, 8, 9], Target(2, 0))
    assert 4 == find([4, 6, 8, 9], [1, 3, 5], Target(2, 0))


def test_find_1():
    assert 2.5 == find([], [2, 3], Target(0, 1))
    assert 2 == find([], [2, 3], Target(0, 0))
    assert 3 == find([], [2, 3], Target(1, 0))


def test_find_2():
    assert 1 == find([2], [1, 3, 5], Target(0, 0))
    assert 2 == find([2], [1, 3, 5], Target(1, 0))
    assert 3 == find([2], [1, 3, 5], Target(2, 0))
    assert 5 == find([2], [1, 3, 5], Target(3, 0))


def test_find_3():
    assert 1.5 == find([2], [1, 3, 5], Target(0, 1))
    assert 2.5 == find([2], [1, 3, 5], Target(1, 1))
    assert 4 == find([2], [1, 3, 5], Target(2, 1))


def test_find_3_swap():
    assert 1.5 == find([1, 3, 5], [2], Target(0, 1))
    assert 2.5 == find([1, 3, 5], [2], Target(1, 1))
    assert 4 == find([1, 3, 5], [2], Target(2, 1))


def test_1():
    sol = Solution()
    assert 2 == sol.findMedianSortedArrays([], [2])
    assert 2 == sol.findMedianSortedArrays([2], [])


def test_2():
    sol = Solution()
    assert 2.5 == sol.findMedianSortedArrays([2], [3])
    assert 2.5 == sol.findMedianSortedArrays([], [2, 3])
    assert 2.5 == sol.findMedianSortedArrays([2, 3], [])


def test_3():
    sol = Solution()
    assert 2 == sol.findMedianSortedArrays([1, 2, 3], [])
    assert 2 == sol.findMedianSortedArrays([1, 3], [2])
    assert 2 == sol.findMedianSortedArrays([1, 2], [3])
    assert 2 == sol.findMedianSortedArrays([3], [1, 2])
    assert 2 == sol.findMedianSortedArrays([2], [1, 3])
    assert 2 == sol.findMedianSortedArrays([1], [2, 3])
