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
        max_id = 0
        def gen_id():
            nonlocal max_id
            max_id += 1
            return max_id
        tree_ids = defaultdict(gen_id)
        count = defaultdict(int)
        result = []
        def dfs(cur):
            if cur is None:
                return None
            tree_id = tree_ids[(cur.val, dfs(cur.left), dfs(cur.right))]
            count[tree_id] += 1
            if count[tree_id] == 2:
                result.append(cur)
            return tree_id

        dfs(root)
        return result


