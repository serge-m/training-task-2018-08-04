"""
975. Odd Even Jump
Hard

"""

from functools import lru_cache


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        self.A = A
        self.n = len(A)
        self.val_idx = sorted([(x, idx) for idx, x in enumerate(A)])
        self.val_idx2 = sorted([(x, idx) for idx, x in enumerate(A)], key=lambda x_idx: (x_idx[0], -x_idx[1]))

        # print(self.val_idx)
        # print(self.val_idx2)

        self.can_jump = [
            [self.next_ge(i) for i in range(0, self.n)],
            [self.next_le(i) for i in range(0, self.n)]
        ]
        # print(self.can_jump)

        # 0 - odd jump
        # 1 - even jump
        dp = [
            [False for i in range(0, self.n)],
            [False for i in range(0, self.n)]
        ]
        dp[0][self.n - 1] = True
        dp[1][self.n - 1] = True
        cnt = 1
        for i in range(self.n - 2, -1, -1):
            for jump_type in [0, 1]:
                nxt = self.can_jump[jump_type][i]
                if nxt is not None:
                    dp[jump_type][i] = dp[1 - jump_type][nxt]
            if dp[0][i]:
                cnt += 1
            # print(i)
            # print(dp)
        return cnt

    def next_ge(self, i):
        pos_in_sorted = bisect.bisect_left(self.val_idx, (self.A[i], -1))
        for j in range(pos_in_sorted + 1, self.n):
            val, idx = self.val_idx[j]
            if idx > i:
                return idx
        return None

    def next_le(self, i):
        # print("next_le", i, self.A[i])
        pos_in_sorted = bisect.bisect_left(self.val_idx2, (self.A[i], 10 ** 10))
        # print("pos_in_sorted", pos_in_sorted, self.val_idx2)
        for j in range(pos_in_sorted - 1, -1, -1):
            val, idx = self.val_idx2[j]
            if idx > i:
                return idx
        return None
