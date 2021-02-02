"""
238. Product of Array Except Self
Medium

t = 12

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_fwd = []
        prev = 1
        for v in nums:
            prev = prev * v
            prods_fwd.append(prev)

        prods_bwd = []
        prev = 1
        for v in nums[::-1]:
            prev = prev * v
            prods_bwd.append(prev)
        prods_bwd = prods_bwd[::-1]

        result = []
        for i in range(len(nums)):
            r = 1
            if i < len(nums) - 1:
                r *= prods_bwd[i + 1]
            if i > 0:
                r *= prods_fwd[i - 1]
            result.append(r)
        return result


"""
1 2 3 4
1 2 6 24

4 12 24 24
24 24 12 4

fwd  1 2 6 24
bwd 24 24 12 4
     0 1  2 3

i = 0
24

i = 1
12 * 1 = 12

i = 2
4 * 2 = 8

i = 3
1 * 6



"""

