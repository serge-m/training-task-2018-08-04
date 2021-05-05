"""
15. 3Sum
Medium

912 ms	17.7 MB
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []
        pos = {x: i for i, x in enumerate(nums)}
        for i in range(n):
            if nums[i] > 0:
                break

            # eliminate duplicate for the first number
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i + 1, n):
                # eliminate duplicates for the second number
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                k = pos.get(-(nums[i] + nums[j]))
                if k is not None and k > j:
                    results.append([nums[i], nums[j], nums[k]])

        return results

