"""
638. Shopping Offers
Medium

Runtime: 152 ms
Memory Usage: 21.6 MB

"""

from typing import List
from functools import lru_cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        def cost_wo_offers(needs):
            return sum((need * p for need, p in zip(needs, price)))

        def subtract(needs, offer):
            return tuple(n - o for n, o in zip(needs, offer))

        @lru_cache(maxsize=None)
        def search(needs):
            if any(need < 0 for need in needs):
                return None
            best = cost_wo_offers(needs)

            for offer in special:
                new_needs = subtract(needs, offer)
                r = search(new_needs)
                if r is not None:
                    best = min(best, r + offer[-1])
            return best

        return search(tuple(needs))
