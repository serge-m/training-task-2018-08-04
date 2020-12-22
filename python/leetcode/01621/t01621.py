from functools import lru_cache
import numpy as np


class Solution:
    def numberOfSets2(self, n: int, k: int) -> int:
        return sum([calc(i, k) for i in range(1, n + 1)], 0) % (10 ** 9 + 7)

    def numberOfSets_with_segm_stat(self, n: int, k: int) -> int:
        return calc_with_segm_stat(n - 1, k, 0)

    def numberOfSets(self, n: int, k: int) -> int:
        return calc_combinatoric(n, k)


def calc_combinatoric(n, k):
    from math import comb
    return comb(n + k - 1, 2 * k) % (10 ** 9 + 7)


@lru_cache(maxsize=None)
def calc_with_segm_stat(n, k, segm_is_going):
    if n == 0:
        if k == 0:
            return 1
        else:
            return 0

    if segm_is_going == 0:
        result = calc_with_segm_stat(n - 1, k, 0) + calc_with_segm_stat(n - 1, k - 1, 1)
    else:
        p1 = calc_with_segm_stat(n - 1, k, 1)  # continue the same segment
        p2 = calc_with_segm_stat(n - 1, k - 1, 1)  # stop the old segment and start a new one
        p3 = calc_with_segm_stat(n - 1, k, 0)  # stop the old segment and make a gap
        result = (
                p1 +
                p2 +
                p3
        )

    return result % (10 ** 9 + 7)


def calc_with_table(n, k):
    table = np.zeros((k + 1, n + 1), dtype='int64')
    table[0][0] = 1
    """
    table[0] = 0

    table[1][1] = 1
    table[1][2] = 2
    table[1][3] = 3
    .....

    table[2][1] = 0
    table[2][2] = table[1][1]
    table[2][3] = table[1][2] + 2 * table[1][1]
    table[2][4] = table[1][3] + 2 * table[1][2] + 3 * table[1][1]
    .....
    """
    modulo = 10 ** 9 + 7
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for len_cur_segm in range(1, j - i + 1 + 1):
                table[i][j] += table[i - 1][j - len_cur_segm] * len_cur_segm
            table[i][j] = table[i][j] % modulo

    result = 0
    for len_first_gap in range(0, n):
        result = (result + table[k, n - 1 - len_first_gap]) % modulo
    return result


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


def test1():
    sol = Solution()
    res = calc_with_table(4, 2)
    res2 = sol.numberOfSets2(4, 2)
    assert res == res2
    res3 = calc_with_segm_stat(4 - 1, 2, 0)
    assert res == res3


def test_calc_with_segm_stat():
    assert calc_with_segm_stat(1, 1, 1) == 1
    assert calc_with_segm_stat(1, 1, 0) == 1
    assert calc_with_segm_stat(1, 0, 0) == 1
    assert calc_with_segm_stat(2, 2, 0) == 1
    assert calc_with_segm_stat(2, 2, 1) == 1
    assert calc_with_segm_stat(2, 1, 0) == 3
    assert calc_with_segm_stat(2, 1, 1) == 4


def test2():
    sol = Solution()
    res = sol.numberOfSets2(10, 7)
    res2 = calc_with_table(10, 7)
    assert res == res2
    res3 = sol.numberOfSets2(10, 7)
    assert res3 == res


def test_c_n_k():
    N = 20
    K = 10
    t2 = np.zeros((N, K), dtype='int')
    t2[1][1] = 1
    for n in range(2, N):
        for k in range(1, K):
            t2[n][k] = t2[n - 1][k - 1] + t2[n - 1][k]

    print(t2)
