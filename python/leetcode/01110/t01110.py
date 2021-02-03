"""
1110. Delete Nodes And Return Forest
Medium


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_del = set(to_delete)

        def dfs(node: TreeNode, start):
            if node is None:
                return None

            deleted = node.val in to_del
            node.left = dfs(node.left, start=deleted)
            node.right = dfs(node.right, start=deleted)

            if deleted:
                return None
            else:
                if start:
                    result.append(node)
                return node


        dfs(root, True)

        return result


"""
1
prev = []

2


"""
