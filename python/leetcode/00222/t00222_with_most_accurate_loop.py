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

        while right >= left:
            mid = (left + right) // 2
            d = probe_depth(root, max_depth, mid)
            # print(left, right, mid, d)
            if d == max_depth:
                left = mid + 1
            else:
                right = mid - 1
        return 2 ** (max_depth - 1) - 1 + int(left)


def get_depth(node):
    depth = 0
    while node is not None:
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


tree7 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5),
                          ),
                 TreeNode(3,
                          TreeNode(6),
                          TreeNode(7),
                          )
                 )

tree6 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5),
                          ),
                 TreeNode(3,
                          TreeNode(6),
                          )
                 )

tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2))
tree1 = TreeNode(1)


def test_get_depth():
    assert get_depth(None) == 0
    assert get_depth(tree1) == 1
    assert get_depth(tree2) == 2
    assert get_depth(tree3) == 2


def test_probe_depth():
    assert probe_depth(None, 1, 0) == 0
    assert probe_depth(tree1, 1, 0) == 1

    assert probe_depth(tree2, 2, 0) == 2
    assert probe_depth(tree2, 2, 1) == 1

    assert probe_depth(tree3, 2, 0) == 2
    assert probe_depth(tree3, 2, 1) == 2

    assert probe_depth(tree6, 3, 0) == 3
    assert probe_depth(tree6, 3, 1) == 3
    assert probe_depth(tree6, 3, 2) == 3
    assert probe_depth(tree6, 3, 3) == 2


def test_count_nodes():
    sol = Solution()
    assert sol.countNodes(tree1) == 1
    assert sol.countNodes(tree2) == 2
    assert sol.countNodes(tree3) == 3
    assert sol.countNodes(tree6) == 6
    assert sol.countNodes(tree7) == 7
