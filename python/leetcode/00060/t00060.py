"""
60. Permutation Sequence
Hard
"""
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return find("", list(range(1, n + 1)), n, k)


def find(solution, elements, n, k):
    # print(solution, elements, n, k)
    if not elements:
        return solution
    s = 0
    cnt_p = math.perm(len(elements) - 1)
    for e in elements:
        if s + cnt_p >= k:
            elements.remove(e)
            return find(solution + str(e), elements, n, k - s)
        s += cnt_p

