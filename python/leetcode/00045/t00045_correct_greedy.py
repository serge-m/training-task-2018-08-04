from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, start, end = 0, 0, 1
        while end < len(nums):
            start, end = end, max(i+nums[i] for i in range(start, end))+1
            steps += 1
        return steps


def test3():
    assert Solution().jump([5, 1, 1, 1, 4, 1, 1, 1, 2, 1, 0]) == 3


def test1():
    assert Solution().jump([5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 0]) == 2


def test2():
    assert Solution().jump([2, 1]) == 1
