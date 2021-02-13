"""
167. Two Sum II - Input array is sorted
Easy
"""
import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n

        while left < right:
            s = numbers[left] + numbers[right - 1]
            if s == target:
                return [left + 1, right]
            left = bisect.bisect_left(numbers, target - numbers[right - 1], lo=left, hi=right)
            right = bisect.bisect_right(numbers, target - numbers[left], lo=left, hi=right)
            # print(left, right)

        return None


"""
  0 1 2 3 4 5 6  7  8 
[-1,0,1,2,3,4,7,11,15]
lr 0 9
lr 0 7
lr 3 7



"""
