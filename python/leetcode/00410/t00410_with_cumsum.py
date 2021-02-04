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
        c_sum = [sum(nums[:i], 0) for i in range(n + 1)]
        # print(dp)
        for num_parts in range(2, m + 1):
            dp_prev = dp
            n1 = n - m + num_parts
            dp = [max_int for i in range(n1)]
            for first_index in range(num_parts - 1, n1):
                cost_of_previous_cuts = dp_prev[first_index - 1]
                for last_index in range(first_index, n1):
                    dp[last_index] = min(
                        dp[last_index],
                        max(c_sum[last_index + 1] - c_sum[first_index], cost_of_previous_cuts)
                    )

            # print(dp)
        return dp[n - 1]
