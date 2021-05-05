"""
15. 3Sum
Medium

Runtime: 1056 ms
Memory Usage: 17.5 MB
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print("nums")
        # print(nums)
        n = len(nums)
        results = []
        for i in range(n):
            if nums[i] > 0:
                break

            # eliminate duplicate for the first number
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                # eliminate duplicates for the second number
                if j > i + 1 and nums[j - 1] == nums[j]:
                    j += 1
                    continue

                # eliminate duplicates for the third number
                if k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                # print(i, j, k)
                c = -(nums[i] + nums[j])
                if c == nums[k]:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif c < nums[k]:
                    k -= 1
                else:  # c > nums[k]
                    j += 1

        return results

