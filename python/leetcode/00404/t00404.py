class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return do_sum(root, False)


def do_sum(root, is_left: bool) -> int:
    if root is None:
        return 0
    if root.left or root.right:
        return do_sum(root.left, True) + do_sum(root.right, False)
    if is_left:
        return root.val
    return 0
