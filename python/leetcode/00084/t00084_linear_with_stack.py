"""
84. Largest Rectangle in Histogram
Hard


"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hs = heights
        n = len(hs)
        s = [-1]
        best = 0

        def add(i, val):
            nonlocal best
            while len(s) > 1 and hs[s[-1]]>= val:
                best = max(best, (i - 1 - s[-2]) * hs[s[-1]] )
                s.pop()
            s.append(i)

        for i in range(n):
            add(i, hs[i])
        add(n, 0)
            # print("i", i, "s", s)
            # print("best", best)
        # print("main end")
        # while len(s) > 1:
        #     best = max(best, (n - 1 - s[-2]) * hs[s[-1]] )
        #     s.pop()
        #     # print(best)
        # print("2nd end")
        return best

