from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = 300
        used = {}
        for x in nums:
            if 0 < x <= N:
                used[x] = 1
        for i in range(1, N + 1):
            if i not in used:
                return i
        return -1

