"""
833. Find And Replace in String
Medium

"""
from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indexes)
        order = sorted(range(0, n), key=lambda i: indexes[i], reverse=True)
        for iop in order:
            source = sources[iop]
            subs_len = len(source)
            start = indexes[iop]
            target = targets[iop]
            if S[start:start + subs_len] == source:
                # replace
                S = S[:start] + target + S[start + subs_len:]
        return S

