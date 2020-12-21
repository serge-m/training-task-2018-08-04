from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return do_search(nums, 0, len(nums) - 1, target)


def do_search(nums, lo, hi, target):
    if lo >= hi - 1:
        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        return -1

    m = lo + (hi - lo) // 2

    if nums[lo] < nums[m]:  # left side is correctly sorted
        if nums[lo] <= target <= nums[m]:
            return do_search(nums, lo, m, target)
        else:
            return do_search(nums, m + 1, hi, target)
    else:  # right side is correctly sorted
        if nums[m] <= target <= nums[hi]:
            return do_search(nums, m, hi, target)
        else:
            return do_search(nums, lo, m - 1, target)



