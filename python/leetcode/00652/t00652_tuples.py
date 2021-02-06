"""
652. Find Duplicate Subtrees
Medium

tree

with tuples, slower
"""

from collections import defaultdict
from functools import lru_cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        traversals = defaultdict(int)
        result = []

        def dfs(cur):
            if cur is None:
                return None

            trav_left = dfs(cur.left)
            trav_right = dfs(cur.right)
            trav = (cur.val, trav_left, trav_right)
            traversals[trav] += 1
            if traversals[trav] == 2:
                result.append(cur)
            return trav

        dfs(root)
        return result


