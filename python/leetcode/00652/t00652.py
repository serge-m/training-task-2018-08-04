"""
652. Find Duplicate Subtrees
Medium

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
        val2nodes = defaultdict(list)
        result = set()

        @lru_cache(maxsize=None)
        def eq(t1, t2):
            if t1 is None:
                return t2 is None

            if t2 is None:
                return False

            return t1.val == t2.val and eq(t1.left, t2.left) and eq(t1.right, t2.right)

        def node2str(n):
            if n is None:
                return "None"
            return f"{n.val}_{id(n) % 777}"

        def p_state(root):
            print("root", node2str(root))
            print("val2nodes", [(k, [node2str(n) for n in v]) for k, v in val2nodes.items()])
            print("result", [node2str(n) for n in result])

        def dfs(root):
            if root is None:
                return
            # p_state(root)

            for node in val2nodes[root.val]:
                if eq(root, node):
                    result.add(node)
                    break
            else:
                val2nodes[root.val].append(root)
            # p_state(root)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return list(result)


"""
root = 1 
val2nodes = {1:[1]}

root = 2
val2nodes = {1:[1], 2:[2]}

root = 4
val2nodes = {1:[1], 2:[2], 4:[4]}

root = 3
val2nodes = {1:[1], 2:[2], 4:[4], 3:[3]}

root = 2
val2nodes = {1:[1], 2:[2], 4:[4], 3:[3]}

eq(2, 2)

e1(4,4) -> true

eq(None,None) -> true
eq(None,None) -> true







"""        
