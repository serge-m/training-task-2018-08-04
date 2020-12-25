from typing import List
import heapq


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_cnt = 10 ** 10
        best_jumps = [max_cnt for i in range(n)]
        q = [(0, 0, 0)]
        while q:
            (cnt_jumps, _, i) = heapq.heappop(q)
            if i == n - 1:
                return cnt_jumps

            new_val = cnt_jumps + 1
            last_jump = min(i + nums[i], n - 1)

            for j in range(last_jump, i, -1):
                if best_jumps[j] > new_val:
                    best_jumps[j] = new_val
                    heapq.heappush(q, (new_val, -j, j))
        return best_jumps[n - 1]
