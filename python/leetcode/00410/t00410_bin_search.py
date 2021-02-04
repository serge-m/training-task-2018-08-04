"""
410. Split Array Largest Sum
Hard

binary search
"""
import math
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def possible_to_cut(size):
            s = 0
            num_splits = 1
            for x in nums:
                if s + x > size:
                    num_splits += 1
                    s = x
                else:
                    s = s + x
            # print("-- ", size, num_splits)
            return num_splits <= m

        left = max(nums)
        right = sum(nums)

        ans = right
        while right - left > 0.25:
            # print(left, right)
            mid = (left + right) / 2
            if possible_to_cut(mid):
                ans = min(ans, mid);
                right = mid
            else:
                left = mid

        return math.floor(mid + 0.5)

