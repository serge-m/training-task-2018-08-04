"""
1268. Search Suggestions System
Medium

"""
from collections import defaultdict
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for p in products:
            t.add(p)

        t.sort()

        result = []
        for i in range(1, len(searchWord) + 1):
            r = t.find(searchWord[:i])
            result.append(r)

        return result


class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.next[c]
        cur.word = word

    def sort(self):
        pass

    def find(self, prefix, max_results=3):
        cur = self.root
        for c in prefix:
            cur = cur.next[c]
        return [c for i, c in zip(range(max_results), self._get_sorted_children(cur))]

    def _get_sorted_children(self, cur):
        if cur.word:
            yield cur.word
        for _, next in sorted(cur.next.items()):
            for w in self._get_sorted_children(next):
                yield w

