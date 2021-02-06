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
            d = probe_depth(root, 0, 2 ** (max_depth - 1) - 1, mid)
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


def probe_depth(node, start, end, leaf_id):
    # print("probe ", node.val if node else node, start, end, leaf_id)
    if node is None:
        return 0
    if start == end:
        if leaf_id == 0:
            return 1
        else:
            return 0
    mid = (start + end) // 2
    if leaf_id <= mid:
        return probe_depth(node.left, start, mid, leaf_id) + 1
    else:
        return probe_depth(node.right, 0, end - (mid + 1), leaf_id - (mid + 1)) + 1


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


def test_count_nodes():
    sol = Solution()
    assert sol.countNodes(tree1) == 1
    assert sol.countNodes(tree2) == 2
    assert sol.countNodes(tree3) == 3
    assert sol.countNodes(tree6) == 6
    assert sol.countNodes(tree7) == 7
