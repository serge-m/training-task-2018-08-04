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

        result = []
        for i in range(1, len(searchWord) + 1):
            r = t.find(searchWord[:i])
            result.append(r)

        return result


ord_a = ord('a')
ord_z = ord('z')

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(ord_a, ord_z+1)]
        self.word = None

    def add(self, c):
        i = ord(c) - ord_a
        if self.children[i] is None:
            self.children[i] = TrieNode()
        return self.children[i]

    def find(self, c):
        i = ord(c) - ord_a
        return self.children[i]

    def dfs(self, cur_word_chars, results, target_len):
        if self.word:
            results.append(''.join(cur_word_chars))
            if len(results) == target_len:
                return True
        for i in range(0, ord_z-ord_a +1):
            if self.children[i] is not None:
                cur_word_chars.append(chr(ord_a+i))
                if self.children[i].dfs(cur_word_chars, results, target_len):
                    return True
                cur_word_chars.pop()

        return False



class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.add(c)
        cur.word = True

    def find(self, prefix, max_results=3):
        cur = self.root
        for c in prefix:
            cur = cur.find(c)
            if cur is None:
                return []

        result = []
        cur.dfs(list(prefix), result, max_results)
        return result


