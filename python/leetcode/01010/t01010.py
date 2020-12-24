"""
1010. Pairs of Songs With Total Durations Divisible by 60
c = medium

"""
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = [t % 60 for t in time]
        m = defaultdict(list)
        for i, rem in enumerate(rems):
            m[rem].append(i)

        cnt_pairs = 0
        for i, rem in enumerate(rems):
            if rem == 0 or rem == 30:
                cnt_pairs += len(m[rem]) - 1  # all other except self
            else:
                rem2 = 60 - rem
                cnt_pairs += len(m[rem2])
        return cnt_pairs // 2  # all the pairs counted twice
