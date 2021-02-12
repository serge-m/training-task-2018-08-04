"""
84. Largest Rectangle in Histogram
Hard


"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hs = heights
        hs.append(0)
        n = len(hs)
        s = [-1]
        best = 0

        for i in range(n):
            while len(s) > 1 and hs[s[-1]] >= hs[i]:
                best = max(best, (i - 1 - s[-2]) * hs[s[-1]])
                s.pop()
            s.append(i)
            # print("i", i, "s", s)
            # print("best", best)
        # print("main end")
        # while len(s) > 1:
        #     best = max(best, (n - 1 - s[-2]) * hs[s[-1]] )
        #     s.pop()
        #     # print(best)
        # print("2nd end")
        return best


"""
0 1 2 3 4 5 6
2 2 0 0 3 3
i=0: 
s=[-1]
s=[-1,0]

i=1
s=[-1,0]
s=[-1,0]
best1 = 1*2 = 2
s=[-1,1]






"""
