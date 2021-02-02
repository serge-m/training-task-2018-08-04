"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        assert len(preorder) == len(inorder)
        pos_inorder = {val: i for i, val in enumerate(inorder)}

        def construct(start_pre, end_pre, start_in, end_in):
            if start_pre >= end_pre or start_pre >= len(preorder):
                return None
            root = TreeNode(val=preorder[start_pre])
            if start_pre + 1 == end_pre:
                return root
            pos_root_inorder = pos_inorder[root.val]
            len_left = pos_root_inorder - start_in
            root.left = construct(start_pre + 1, start_pre + len_left + 1, start_in, pos_root_inorder)
            root.right = construct(start_pre + len_left + 1, end_pre, pos_root_inorder + 1, end_in)
            return root

        return construct(0, len(preorder), 0, len(inorder))


"""
idx 0 1 2
pre 1 2 3
in  3 2 1

0 3 0 3
pos = 2

left 
1 3 0 2
pos = 1

left 
2 


  1
2


pre 3 9 29 15 7
in  9 3 15 20 7

pre 9 
in  9 



"""
