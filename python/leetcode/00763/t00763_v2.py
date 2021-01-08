"""
763. Partition Labels
Medium

t=15
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        N = len(S)
        if N == 0:
            return []

        word_end = fill_word_end(S, N)
        return recover_lengths(word_end)


def fill_word_end(S, N):
    word_start = [-1 for c in S]
    word_end = [-1 for c in S]
    first_pos = dict()
    for i in range(0, N):
        first_pos.setdefault(S[i], i)

    for i in range(0, N):
        prev_i = first_pos[S[i]]
        if prev_i == i: # new symbol, start new word
            word_start[i] = i
        else:
            word_start[i] = word_start[prev_i]
        word_end[word_start[i]] = i # update end
        word_end[i] = i


    return word_end


def recover_lengths(word_end):
    res = []
    i = 0
    while i < len(word_end):
        res.append((word_end[i] + 1) - i)
        i = word_end[i] + 1
    return res
