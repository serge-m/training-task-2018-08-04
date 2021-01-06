"""
763. Partition Labels
Medium

t=41
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        N = len(S)
        if N == 0:
            return []

        partition_start = forward_fill_score(S, N)

        return backward_recover_lengths(partition_start)


def forward_fill_score(S, N):
    partition_start = [-1 for c in S]
    first_pos = dict()
    for i in range(0, N):
        p = first_pos.get(S[i])
        if p is None:
            # start new partition
            first_pos[S[i]] = i
            partition_start[i] = i
        else:
            for j in range(p + 1, i + 1):
                partition_start[j] = partition_start[p]

    return partition_start


def backward_recover_lengths(partition_start):
    i = len(partition_start) - 1
    res = []
    while i >= 0:
        res.append(i - partition_start[i] + 1)
        i = partition_start[i] - 1
    return res[::-1]
