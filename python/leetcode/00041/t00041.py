from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = 300
        first_N = list(range(N + 1))
        for x in nums:
            if 0 < x <= N:
                first_N[x] = 0
        for i in first_N:
            if i != 0:
                return i
        return -1

