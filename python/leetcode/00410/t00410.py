"""
410. Split Array Largest Sum
Hard
"""
from functools import lru_cache


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def sum_nums(start, end):
            return sum(nums[start:end])

        def best_split(dp_prev, num_parts, last_idx_in_array):
            best = None
            for last_idx_of_prev_split in range(0, last_idx_in_array):
                if num_parts - 2 > last_idx_of_prev_split:
                    continue
                sum_last_part = sum_nums(last_idx_of_prev_split + 1, last_idx_in_array + 1)
                sum_of_split = max(sum_last_part, dp_prev[last_idx_of_prev_split])
                if best is None or best > sum_of_split:
                    best = sum_of_split
            return best

        dp = [sum(nums[:i + 1]) for i in range(n)]
        # print(dp)
        for num_parts in range(2, m + 1):
            dp_prev = dp[:]
            # dp = [0 for  i in range(n)]
            for last_idx_in_array in range(n):
                # current array is nums[:last_idx_in_array+1], must be split into num_parts parts
                dp[last_idx_in_array] = best_split(dp_prev, num_parts, last_idx_in_array)
            # print(dp)
        return dp[n - 1]
