"""
53. Maximum Subarray
Easy

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[:]
        for i in range(len(nums)):
            if i > 0:
                best[i] = max(best[i], best[i - 1] + nums[i])

        return max(best)



