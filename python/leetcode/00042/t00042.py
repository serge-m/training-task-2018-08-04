from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        max_left = [0 for i in range(n)]
        max_left[0] = 0
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        max_right = [0 for i in range(n)]
        max_right[n - 1] = 0
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        water = 0
        for i in range(n):
            add_water = min(max_left[i], max_right[i]) - height[i]
            water += max(0, add_water)
        return water


def test_1():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_2():
    assert Solution().trap([]) == 0
    assert Solution().trap([1]) == 0
    assert Solution().trap([10]) == 0
    assert Solution().trap([1, 2]) == 0
    assert Solution().trap([1, 2, 3]) == 0
