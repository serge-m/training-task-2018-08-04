# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        best_dist = None
        prev = None
        for i in search(root):
            if prev is not None:
                if best_dist is None or i - prev < best_dist:
                    best_dist = i - prev
            prev = i
        return best_dist


def search(root):
    if root is None:
        return
    for i in search(root.left):
        yield i
    yield root.val
    for i in search(root.right):
        yield i


