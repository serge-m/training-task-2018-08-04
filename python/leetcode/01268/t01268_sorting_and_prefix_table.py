"""
1268. Search Suggestions System
Medium

"""
from collections import defaultdict
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix_table = defaultdict(list)  # table prefix -> list of words.

        for p in products:
            # add all prefixes to the table
            for i in range(len(p)):
                # added in sorted order because products are sorted
                prefix_table[p[:i + 1]].append(p)

        result = []
        max_results = 3
        for i in range(len(searchWord)):
            # search by prefix
            r = prefix_table[searchWord[:i + 1]][:max_results]
            result.append(r)
        return result
