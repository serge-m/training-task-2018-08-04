"""
107. Binary Tree Level Order Traversal II
Easy
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

        if root is None:
            return []

        next_layer = [(root, 0)]

        while next_layer:
            cur_layer, next_layer = next_layer, []
            cur_result = []
            for cur, level in cur_layer:
                cur_result.append(cur.val)
                if cur.left:
                    next_layer.append((cur.left, level + 1))
                if cur.right:
                    next_layer.append((cur.right, level + 1))

            result.append(cur_result)

        return result[::-1]
