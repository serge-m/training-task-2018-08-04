"""
239. Sliding Window Maximum
Hard
"""

from collections import deque
from typing import List
import bisect


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window_val_idxs = deque()
        len_win = 0
        n = len(nums)

        def get_max():
            return -window_val_idxs[0][0]

        def remove_prev_start():
            nonlocal len_win
            if len_win > 0 and prev_start == window_val_idxs[0][1]:
                window_val_idxs.popleft()
                len_win -= 1

        def add_end():
            nonlocal len_win
            pos = bisect.bisect_left(window_val_idxs, (-nums[end], end), hi=len_win)
            window_val_idxs.insert(pos, (-nums[end], end))
            len_win = pos + 1

        result = []
        for end in range(n):
            prev_start = end - k
            remove_prev_start()
            add_end()
            if prev_start >= -1:
                result.append(get_max())

        return result


