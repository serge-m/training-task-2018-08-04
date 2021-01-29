"""
1268. Search Suggestions System
Medium

Runtime: 1784 ms, faster than 5.04% of Python3 online submissions for Search Suggestions System.
Memory Usage: 23.4 MB, less than 5.45% of Python3 online submissions for Search Suggestions System.

"""
from collections import defaultdict
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for p in products:
            t.add(p)

        result = []
        chars_in_prefix = []
        cur = t.root
        for c in searchWord:
            chars_in_prefix.append(c)
            cur, r = t.find(cur, chars_in_prefix, c)
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

    def find(self, cur, chars_in_prefix, c, max_results=3):
        #print(cur, chars_in_prefix, c)
        if cur is None:
            return None, []
        cur = cur.find(c)
        if cur is None:
            return None, []

        result = []
        cur.dfs(chars_in_prefix[:], result, max_results)
        return cur, result


