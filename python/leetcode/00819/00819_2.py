"""
819. Most Common Word
Easy

version 2
"""
from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = defaultdict(int)
        banned = set(banned)
        for word in split(remove_punctuation(paragraph)):
            word = word.lower()
            if word not in banned:
                counter[word] += 1

        max_pair = max(counter.items(), key=lambda k_v: k_v[1])
        return max_pair[0]


def remove_punctuation(paragraph):
    punctuation = set("!?',;.")
    for c in paragraph:
        if c not in punctuation:
            yield c
        else:
            yield " "


def split(paragraph):
    word = []
    for c in paragraph:
        if c != ' ':
            word.append(c)
        else:
            if word:
                yield ''.join(word)
                word = []

    if word:
        yield ''.join(word)
