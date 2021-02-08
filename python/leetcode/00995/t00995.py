"""
995. Minimum Number of K Consecutive Bit Flips
Hard
"""


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        f = [0 for i in range(n + 1)]

        def flip(start):
            f[start + K] = 1 - f[start + K]

        # print(f)
        cnt = 0
        cur_good = 1
        for i in range(n - K + 1):
            if f[i]:
                cur_good = 1 - cur_good
            if A[i] == cur_good:
                pass
            else:
                cur_good = 1 - cur_good
                flip(i)
                cnt += 1
            # print("cur_good", cur_good)
            # print("f", f)

        for i in range(n - K + 1, n):
            if f[i]:
                cur_good = 1 - cur_good
            if A[i] != cur_good:
                return -1
        return cnt


"""
k= 3
1111111111
1100011111
1100010001
1100101001
1011101001
0101101001

1100101001
1111001001
1111110001


0101101001
1011101001
1100101001
1111001001
1111110001

"""
