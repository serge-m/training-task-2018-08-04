"""
792. Number of Matching Subsequences
Medium
"""
from collections import Counter


class Solution(object):

    def numMatchingSubseq(self, S, words):

        pointers = {
            ' ': [iter(w) for w in words]
        }

        result = 0

        def step(c):
            nonlocal result
            for it in pointers.pop(c, []):
                try:
                    next_c = next(it)
                    pointers.setdefault(next_c, []).append(it)
                except StopIteration:
                    result += 1

        step(' ')
        for c in S:
            step(c)
        return result
