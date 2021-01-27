"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Medium

t = 12
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts.append(h)
        verticalCuts.append(w)

        return (
                       (max_diff(horizontalCuts) % (10 ** 9 + 7)) *
                       (max_diff(verticalCuts) % (10 ** 9 + 7))
               ) % (10 ** 9 + 7)


def max_diff(sorted_list):
    best_diff = sorted_list[0]
    for i in range(1, len(sorted_list)):
        diff = sorted_list[i] - sorted_list[i - 1]
        if diff > best_diff:
            best_diff = diff

    return best_diff
