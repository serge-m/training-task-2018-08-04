"""
34. Find First and Last Position of Element in Sorted Array
Medium

binary search
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        lower_bound = left
        if lower_bound >= n or nums[lower_bound] != target:
            return [-1, -1]

        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        upper_bound = left - 1

        return [lower_bound, upper_bound]


"""
upper

i    0 1
nums 2
tar  2
mi 1
lr (1,1)
ok

i    0 1
nums 2
tar  1
mi 1
lr (0,0)
ok

i    0 1
nums 2
tar  3
mi 1
lr (1,1)
ok


i    0 1 2
nums 0 2
target 2
mi 1
lr (1,2)
mi 1
lr (2,2)


i    0 1 2
nums 0 2
target 0
mi 1
lr 0, 1
mi 0
lr 1 1 
ok

i    0 1 2
nums 0 2
target -1
mi 1
lr 0 1
mi 0 
lr 0 0
ok

i    0 1 2
nums 0 2
target 1
mi 1 
lr 0 1
mi 0
lr 1 1 
ok

i    0 1 2
nums 0 2
target 3
mi 1
lr 1, 2
mi 1
lr 2 ,2 
ok

---------------------------
lower
i    0 1 2
nums 0 2
target 2
mi 1
lr (0, 1)
mi 0
lr (1,1)
ok

i    0 1 2
nums 0 2
target 0
mi 1
lr (0, 1)
mi 0
lr (0, 0)
ok



i    0 1 2
nums 0 2
target -1
mi 1
lr 0 1
mi 0
lr 0 0 

i    0 1 2
nums 0 2
target 1
mi 1
lr 0 1
mi 0
lr 1 1



i    0 1 2
nums 0 2
target 3
mi 1
lr 2 2 




"""
