"""
107. Binary Tree Level Order Traversal II
Easy
t=13
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        q = deque()

        if root is None:
            return []

        q.append((root, 0))

        while q:
            cur, level = q.popleft()
            while len(result) <= level:
                result.append([])
            result[level].append(cur.val)

            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))

        return result[::-1]
