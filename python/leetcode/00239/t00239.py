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
        window_idxs = deque()

        n = len(nums)

        def get_max():
            return nums[window_idxs[0]]

        def remove_prev_start():
            if window_idxs and prev_start == window_idxs[0]:
                window_idxs.popleft()

        def add_end():
            while window_idxs and nums[end] >= nums[window_idxs[-1]]:
                window_idxs.pop()
            window_idxs.append(end)

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





==================
s -2
e 1
w [1]

s -1
e 2
w [1, 2]

s 0
e 3
r += 3 // nums[1]
w [1, 2, 3]

s 1
e 4
r += 3 // nums[1]
w [4]

s 2
e 5
r += 5 // nums[4]
w [4(5), 5(3)]


s 3
e 6
r += 5 // nums[4]
w [6(6)]



s 4
e 7
r += 6 // nums[6]
w [7(7)]




"""
