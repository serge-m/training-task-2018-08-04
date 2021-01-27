"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Medium

"""

import itertools
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts = itertools.chain([0], horizontalCuts, [h])
        verticalCuts = itertools.chain([0], verticalCuts, [w])
        mdh = max_diff(horizontalCuts)
        mdv = max_diff(verticalCuts)
        m = 10 ** 9 + 7
        return ((mdh % m) * (mdv % m)) % m


def max_diff(sorted_list):
    best_diff = -1
    prevs, curs = itertools.tee(sorted_list, 2)
    next(curs, False)
    for prev, cur in zip(prevs, curs):
        diff = cur - prev
        if diff > best_diff:
            best_diff = diff

    return best_diff
