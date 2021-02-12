"""
84. Largest Rectangle in Histogram
Hard

t=18
O(n**2)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hs = heights
        n = len(hs)
        s = [-1]
        best = 0
        for i in range(n):
            while len(s) > 1 and hs[s[-1]] >= hs[i]:
                s.pop()
            s.append(i)
            for j in range(1, len(s)):
                best = max(best, (i - s[j - 1]) * hs[s[j]])
            # print(i, best)
        return best
