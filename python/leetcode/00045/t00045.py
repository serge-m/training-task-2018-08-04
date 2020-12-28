from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_cnt = 10 ** 10
        jumps = [max_cnt for _ in nums]
        jumps[0] = 0
        for i in range(n):
            new_val = jumps[i] + 1
            last_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, last_jump + 1):
                if jumps[j] > new_val:
                    jumps[j] = new_val
                if j == n - 1:
                    return jumps[n - 1]

        return jumps[n - 1]


def test1():
    nums = list(map(int, "5 1 1 1 1 5 1 1 1 1 0".split(' ')))
    assert Solution().jump(nums) == 2
