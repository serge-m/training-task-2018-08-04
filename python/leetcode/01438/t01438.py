"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

too slow
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        longest_size = 1

        for start in range(0, n):
            min_val = min(nums[start:start + longest_size])
            max_val = max(nums[start:start + longest_size])
            for end in range(start + longest_size, n):  # end is included
                min_val = min(min_val, nums[end])
                max_val = max(max_val, nums[end])
                if max_val - min_val <= limit:
                    longest_size = max(longest_size, end - start + 1)
                else:
                    break
        return longest_size

