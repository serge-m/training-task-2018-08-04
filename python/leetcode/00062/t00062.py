import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return count_paths(m, n)


@functools.lru_cache(maxsize=None)
def count_paths(m, n):
    if m < 0 or n < 0:
        return 0
    if (m, n) == (1, 1):
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)


def test_count_paths():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{count_paths(i, j):4d}", end=" ")
        print()
