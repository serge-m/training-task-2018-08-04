"""
45. Jump Game II

Solution with segment tree

"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_jump = 10 ** 10
        st = SegmentTree(n, op=min, start_elem=max_jump)
        st.update(0, 0)
        for i in range(1, n):
            best = st.compute(i - nums[n-1-i], i) + 1
            st.update(i, best)

        return st.compute(n - 1, n - 1)


class SegmentTree:
    def __init__(self, n, op=min, start_elem=10 ** 10):
        self.n = n
        self._data = [start_elem for i in range(4 * self.n)]
        self._op = op
        self._start_elem = start_elem


    def _compute(self, root, tl, tr, l, r):
        if l > r:
            return self._start_elem

        if l == tl and r == tr:
            return self._data[root]

        tm = (tl + tr) // 2
        return self._op(
            self._compute(root * 2, tl, tm, l, min(r, tm)),
            self._compute(root * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        )

    def compute(self, l, r):
        return self._compute(1, 0, self.n - 1, max(0, l), min(r, self.n-1))

    def _update(self, root, tl, tr, pos, new_val) -> None:
        if tl == tr:
            self._data[root] = new_val
            return
        tm = (tl + tr) // 2
        if pos <= tm:
            self._update(root * 2, tl, tm, pos, new_val)
        else:
            self._update(root * 2 + 1, tm + 1, tr, pos, new_val)
        self._data[root] = self._op(
            self._data[root * 2],
            self._data[root * 2 + 1],
        )

    def update(self, pos, new_val):
        return self._update(1, 0, self.n - 1, pos, new_val)


def test1():
    assert Solution().jump([5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 0]) == 2


def test2():
    assert Solution().jump([2, 1]) == 1
