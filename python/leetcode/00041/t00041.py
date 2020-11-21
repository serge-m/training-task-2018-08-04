from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sort1(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


def sort1(nums):
    for i in range(len(nums)):
        while True:
            pos_for_cur = nums[i] - 1
            if pos_for_cur == i:  # the number is on it's place
                break
            if pos_for_cur < 0 or pos_for_cur >= len(nums):  # the number is out of range, no need to sort
                break
            if nums[i] == nums[pos_for_cur]:  # it's a duplicate, skip
                break
            nums[i], nums[pos_for_cur] = nums[pos_for_cur], nums[i]


def test_2():
    assert Solution().firstMissingPositive([-2, 2, 3, 0, -1]) == 1


def test_3():
    assert Solution().firstMissingPositive([2, 3, 1, 5]) == 4


def test_4():
    assert Solution().firstMissingPositive([2, 3, 1, 4]) == 5


def test_5():
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2


def test_6():
    assert Solution().firstMissingPositive([1, 1, 3]) == 2
    assert Solution().firstMissingPositive([1, 1, 2]) == 3
    assert Solution().firstMissingPositive([1, 1]) == 2


def test_7():
    assert Solution().firstMissingPositive([0, -1, 3, 1]) == 2


def test_8():
    assert Solution().firstMissingPositive([0, 2, 2, 1, 1]) == 3
