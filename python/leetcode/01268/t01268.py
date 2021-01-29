"""
1268. Search Suggestions System
Medium

t = 8
"""
from collections import defaultdict
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = PrefixTable()
        for p in products:
            t.add(p)

        t.sort()

        result = []
        for i in range(1, len(searchWord) + 1):
            r = t.find(searchWord[:i])
            result.append(r)

        return result


class PrefixTable:
    def __init__(self):
        self.data = defaultdict(list)

    def add(self, word):
        for i in range(1, len(word) + 1):
            self.data[word[:i]].append(word)

    def sort(self):
        for k, v in self.data.items():
            v.sort()

    def find(self, prefix, max_results=3):
        return self.data[prefix][:max_results]
