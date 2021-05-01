"""
15. 3Sum
Medium

O(n^2)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = set()
        pos = {x: i for i, x in enumerate(nums)}
        for i in range(n):
            for j in range(i + 1, n):
                k = pos.get(-(nums[i] + nums[j]))
                if k is not None and k > j:
                    results.add((nums[i], nums[j], nums[k]))

        return [list(triplet) for triplet in results]
