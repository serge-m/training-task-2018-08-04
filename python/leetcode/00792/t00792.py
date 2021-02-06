"""
792. Number of Matching Subsequences
Medium


string matching
"""

from collections import Counter


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        res = 0

        def match(s, w):
            i_start = 0
            for cw in w:
                for i in range(i_start, len(s)):
                    if cw == s[i]:
                        i_start = i + 1
                        break
                else:
                    return False
            return True

        counter = Counter(words)
        for w in counter.keys():
            if match(S, w):
                res += counter[w]
        return res
