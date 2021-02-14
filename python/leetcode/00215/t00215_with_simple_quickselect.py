"""
215. Kth Largest Element in an Array
Medium

with simple quick select
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cur = nums
        while len(cur) > 1:
            pivot = cur[random.randint(0, len(cur) - 1)]
            less = []
            len_eq = 0
            larger = []
            for x in cur:
                if x == pivot:
                    len_eq += 1
                elif x < pivot:
                    less.append(x)
                else:
                    larger.append(x)
            if k <= len(larger):
                # k is the same
                cur = larger
            elif k <= len(larger) + len_eq:
                return pivot
            else:
                k -= len(larger) + len_eq
                cur = less
        return cur[0]

