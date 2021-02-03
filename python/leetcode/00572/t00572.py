"""
572. Subtree of Another Tree
Easy

t=8
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def match(s, t):
            if s is None:
                return t is None
            if t is None:
                return False
            return s.val == t.val and match(s.left, t.left) and match(s.right, t.right)

        def dfs(s, t):
            if s is None:
                return t is None
            if match(s, t):
                return True
            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)
