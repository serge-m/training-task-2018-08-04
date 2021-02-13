"""
probably wrong
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        lower_bound = left
        if nums[lower_bound] != target:
            return [-1, -1]

        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        upper_bound = right

        return [lower_bound, upper_bound]


"""

upper not found
i    0 1 2
nums 0 2 4
target 1.5
mid i 1
lr (0, 0)
ret null


upper not found
i    0 1 2
nums 0 2 4
target 2.5
mid i 1
lr (1, 2)
mid i 1
loop :(


lower not found
i    0 1 2
nums 0 2 4
target 1.5
mid i 1
lr (0, 1)
mi 0
lr (1, 1)
ret null

lower not found
i    0 1 2
nums 0 2 4
target -5
mid i 1
lr (0, 1)
mi 0
lr (0, 0)
ret null


lower 
i    0 1 2
nums 0 2 4
target 2
mid i 1
lr (0, 1)
mi 0
lr (1,1)


i    0 1 
nums 0 2
target 2
mi 0
lr (1, 1)

i    0 1 
nums 0 2
target 0
mi 0
lr (0, 0)


i    0 1 
nums 0 2
target -1
mi 0
lr (0, 0)
ok

i    0 1 
nums 0 2
target 1
mi 0
lr (1, 1)
ok

i    0 1 
nums 0 2
target 3
mi 0
lr (1, 1)
ok



"""
