"""
31. Next Permutation
Medium
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        p = find_first_non_inversion(nums)
        if p > 0:
            target = find_pos_in_inversion(nums, p - 1)
            swap(nums, p - 1, target)
        inverse(nums, p, N - 1)


def inverse(nums, start, end):
    i_to = end
    i_from = start
    while i_from < i_to:
        swap(nums, i_from, i_to)
        i_from += 1
        i_to -= 1


def find_pos_in_inversion(nums, p):
    N = len(nums)
    for i in range(N - 1, p, -1):
        if nums[i] > nums[p]:
            return i
    return p


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def find_first_non_inversion(nums):
    N = len(nums)
    for i in range(N - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            return i
    return 0
