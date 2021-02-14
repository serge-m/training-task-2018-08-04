"""
128. Longest Consecutive Sequence
Hard
"""
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        adj = defaultdict(set)
        for x in nums:
            adj[x].add(x + 1)
            adj[x].add(x - 1)

        visited = set()

        def dfs(u):
            visited.add(u)
            longest1 = 0
            longest2 = 0

            while adj[u]:
                v = adj[u].pop()
                if v in adj and v not in visited:
                    len_path = dfs(v)
                    if len_path >= longest1:
                        longest2 = longest1
                        longest1 = len_path
                    elif len_path >= longest2:
                        longest2 = len_path

            return longest1 + 1 + longest2

        return max(
            (
                dfs(x)
                for x in nums
            ),
            default=0
        )
