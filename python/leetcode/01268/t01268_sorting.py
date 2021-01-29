"""
Runtime: 80 ms, faster than 84.31% of Python3 online submissions for Search Suggestions System.
Memory Usage: 17.1 MB, less than 69.07% of Python3 online submissions for Search Suggestions System.
"""

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for x in range(len(searchWord)):
            word = searchWord[:x+1]
            products = [item for item in products if item.startswith(word)]
            result.append(products[:3])
        return result
