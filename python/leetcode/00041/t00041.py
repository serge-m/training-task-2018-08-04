from typing import List


def move_negative_to_end(nums):
    i_end = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= 0:
            nums[i], nums[i_end] = nums[i_end], nums[i]
            i_end -= 1
    return i_end + 1, nums


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i_end, nums = move_negative_to_end(nums)
        if i_end == 0:
            return 1
        min_num = min(nums[:i_end])
        if min_num > 1:
            return 1
        for i in range(i_end):
            while nums[i] != i + 1:
                cur = nums[i]
                pos_for_cur = cur - 1
                if pos_for_cur < i:

                if pos_for_cur < 0 or pos_for_cur >= len(nums):
                    return i + 1

                nums[i], nums[pos_for_cur] = nums[pos_for_cur], nums[i]

        return i_end + 1


def test_1():
    i_end, res = move_negative_to_end([-2, 2, 3, 0, -1])
    assert set(res[:i_end]) == {2, 3}
    i_end, res = move_negative_to_end([4, 5])
    assert set(res[:i_end]) == {4, 5}
    i_end, res = move_negative_to_end([0, 4, 5])
    assert set(res[:i_end]) == {4, 5}
    i_end, res = move_negative_to_end([4, -1, 5])
    assert set(res[:i_end]) == {4, 5}
    i_end, res = move_negative_to_end([4, 4, -1, 5])
    assert sorted(res[:i_end]) == [4, 4, 5]


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
