"""
103. Binary Tree Zigzag Level Order Traversal
Medium


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
             return []
        prev_layer = []
        next_layer = [root]
        result = [[root.val]]
        direction = 1
        while next_layer:
            prev_layer = next_layer
            next_layer = []
            for node in prev_layer:
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            if next_layer:
                if direction == 0:
                    result.append([n.val for n in next_layer])
                else:
                    result.append([n.val for n in next_layer[::-1]])
            direction = 1 - direction

        return result
