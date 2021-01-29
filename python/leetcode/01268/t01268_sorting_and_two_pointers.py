"""
Runtime: 76 ms, faster than 88.70% of Python3 online submissions for Search Suggestions System.
Memory Usage: 17.3 MB, less than 31.89% of Python3 online submissions for Search Suggestions System.

"""

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        start = 0
        n = len(products)
        end = n - 1
        for x in range(len(searchWord)):
            while start <= end and (len(products[start]) <= x or products[start][x] < searchWord[x]):
                start += 1
            while start <= end and (len(products[end]) <= x or products[end][x] > searchWord[x]):
                end -= 1

            p = [products[i] for i in range(start, min(start + 3, end + 1))]
            result.append(p)
        return result
