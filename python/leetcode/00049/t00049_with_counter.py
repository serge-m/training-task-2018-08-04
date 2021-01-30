"""
49. Group Anagrams
Medium

"""

from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        empty_counts = {c: 0 for c in letters}
        for w in strs:
            c = Counter(empty_counts)
            c.update(w)
            k = tuple(c.values())
            groups[k].append(w)

        return list(groups.values())
