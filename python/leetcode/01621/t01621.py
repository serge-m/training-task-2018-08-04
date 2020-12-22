from functools import lru_cache
import numpy as np


class Solution:
    def numberOfSets2(self, n: int, k: int) -> int:
        return sum([calc(i, k) for i in range(1, n + 1)], 0) % (10 ** 9 + 7)

    def numberOfSets(self, n: int, k: int) -> int:
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
    res = sol.numberOfSets(4, 2)
    res2 = sol.numberOfSets2(4, 2)
    assert  res == res2


def test2():
    sol = Solution()
    res = sol.numberOfSets(10, 7)
    res2 = sol.numberOfSets2(10, 7)
    assert  res == res2


def test_c_n_k():
    N = 20
    K = 10
    t2 = np.zeros((N, K), dtype='int')
    t2[1][1] = 1
    for n in range(2, N):
        for k in range(1, K):
            t2[n][k] = t2[n-1][k-1] + t2[n-1][k]

    print(t2)
