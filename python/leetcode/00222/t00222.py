"""
222. Count Complete Tree Nodes
Medium
"""

# Definition for a binary tree node.
try:
    TreeNode
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        max_depth = get_depth(root)
        if max_depth == 0:
            return 0

        left = 0
        right = 2 ** (max_depth - 1) - 1

        while right > left:
            mid = (left + right) // 2
            d = probe_depth(root, max_depth, mid)
            print(left, right, mid, d)
            if d == max_depth:
                if left == mid:
                    print("asdasd")
                    break
                left = mid

            else:
                right = mid
        if probe_depth(root, max_depth, right) == max_depth:
            return 2 ** (max_depth - 1) - 1 + right + 1
        else:
            return 2 ** (max_depth - 1) - 1 + left + 1


def get_depth(node):
    depth = 0
    while node != None:
        node = node.left
        depth += 1
    return depth


def probe_depth(node, depth, child_id):
    if node is None:
        return 0
    if depth == 1:
        return 1
    cnt_in_left = 2 ** (depth - 2)
    if child_id < cnt_in_left:
        return probe_depth(node.left, depth - 1, child_id) + 1
    else:
        return probe_depth(node.right, depth - 1, child_id - cnt_in_left) + 1


def test_get_depth():
    assert get_depth(None) == 0
    assert get_depth(TreeNode(1)) == 1
    assert get_depth(TreeNode(1, TreeNode(2))) == 2
    assert get_depth(TreeNode(1, TreeNode(2), TreeNode(3))) == 2


def test_get_depth():
    assert probe_depth(None, 1, 0) == 0
    assert probe_depth(TreeNode(1), 1, 0) == 1
    assert probe_depth(TreeNode(1, TreeNode(2)), 2, 0) == 2
    assert probe_depth(TreeNode(1, TreeNode(2)), 2, 1) == 1
    assert probe_depth(TreeNode(1, TreeNode(2), TreeNode(3)), 2, 0) == 2
    assert probe_depth(TreeNode(1, TreeNode(2), TreeNode(3)), 2, 1) == 2
