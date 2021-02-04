"""
1705. Maximum Number of Eaten Apples
Medium


"""

from typing import List
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        stash = []

        def add(expiry, a, ):
            heapq.heappush(stash, (expiry, a))

        def remove_rotten(i):
            while stash and stash[0][0] <= i:
                heapq.heappop(stash)

        def get_apple():
            if not stash:
                return 0
            expiry, a = heapq.heappop(stash)
            a -= 1
            if a > 0:
                heapq.heappush(stash, (expiry, a))
            return 1

        i = 0
        result = 0
        while True:
            if i < len(apples) and apples[i] != 0:
                add(i + days[i], apples[i], )
            remove_rotten(i)
            result += get_apple()
            if i >= len(apples) and not stash:
                break
            i += 1
        return result
