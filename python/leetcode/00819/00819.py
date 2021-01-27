"""
819. Most Common Word
Easy

t = 12
"""
from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = defaultdict(int)
        banned = set(banned)
        for word in split(paragraph):
            word = word.strip()
            word = word.lower()
            if word in banned:
                continue
            counter[word] += 1

        max_pair = max((val, w) for w, val in counter.items())
        return max_pair[1]


def split(paragraph):
    spaces = set("!?',;. ")
    i = 0
    n = len(paragraph)
    while i < n:
        while i < n and paragraph[i] in spaces:
            i += 1
        word_start = i  # first non space
        while i < n and paragraph[i] not in spaces:
            i += 1
        # i - first space
        if word_start < i:
            yield paragraph[word_start:i]
