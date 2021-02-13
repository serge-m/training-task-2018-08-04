"""
11. Container With Most Water
Medium

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1
        best = 0
        while l < r:
            best = max(best, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                if height[l + 1] > height[r - 1]:
                    l += 1
                else:
                    r -= 1

        return best


"""
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
lr 0 8
best = 7
lr 1 8
best = 49


"""
