"""
239. Sliding Window Maximum
Hard
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window_idxs = list()
        w_start, w_end = 0, 0

        n = len(nums)

        def get_max():
            return nums[window_idxs[w_start]]

        def remove_prev_start():
            nonlocal w_start, w_end
            if w_end > w_start and prev_start == window_idxs[w_start]:
                w_start += 1

        def add_end():
            nonlocal w_start, w_end
            while w_end > w_start and nums[end] >= nums[window_idxs[w_end-1]]:
                w_end -= 1
            if w_end >= len(window_idxs):
                window_idxs.append(end)
            else:
                window_idxs[w_end] = end
            w_end += 1

        result = []
        for end in range(n):
            prev_start = end - k
            remove_prev_start()
            add_end()
            if prev_start >= -1:
                result.append(get_max())

        return result

"""
[1,3,-1,-3,5,3,6,7]
3

w []

s -2  e 0
w [0(1)]

s -1  e 1
w [1(3)]

s 0  e 2
w [1(3), 2(-1)]
r + 3

s 1  e 3
w [1(3), 2(-1), 3(-3)]
r += 3

s 2  e 4
w [4(5)]
r += 5

"""
