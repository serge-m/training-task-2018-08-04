from functools import lru_cache


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return sum([calc(i, k) for i in range(1, n + 1)], 0) % (10 ** 9 + 7)


@lru_cache(maxsize=None)
def calc(n, k):
    """
    count number of ways with a segment starting right at n-1"""
    if k == 1:
        if n > 0:
            return n - 1
        else:
            return 0

    if n - 1 < k:
        return 0
    if n - 1 == k:
        return 1

    res = 0
    for total_len in range(1, n):
        num_gap_variants = total_len
        res += num_gap_variants * calc(n - total_len, k - 1)
    return res % (10 ** 9 + 7)


