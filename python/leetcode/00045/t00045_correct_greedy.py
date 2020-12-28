from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, start, end = 0, 0, 1
        while end < len(nums):
            start, end = end, max(i+nums[i] for i in range(start, end))+1
            steps += 1
        return steps
