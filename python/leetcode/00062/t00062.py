import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return count_paths(m, n)


@functools.cache
def count_paths(m, n):
    if m < 0 or n < 0:
        return 0
    if (m, n) == (1, 1):
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)
