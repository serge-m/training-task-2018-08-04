"""
410. Split Array Largest Sum
Hard
"""
from functools import lru_cache


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        max_int = 10 ** 10

        dp = [sum(nums[:i + 1]) for i in range(n)]
        # print(dp)
        for num_parts in range(2, m + 1):
            dp_prev = dp
            dp = [max_int for i in range(n)]
            for first_index in range(num_parts - 1, n):
                cost_of_previous_cuts = dp_prev[first_index - 1]
                s = 0
                for last_index in range(first_index, n):
                    s += nums[last_index]
                    dp[last_index] = min(dp[last_index], max(s, cost_of_previous_cuts))

            # print(dp)
        return dp[n - 1]
