"""
133. Clone Graph
Medium

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old2new = {}

        def deepcopy(node):
            nonlocal old2new
            if node is None:
                return None
            if node in old2new:
                return old2new[node]

            copy = Node(
                node.val
            )
            old2new[node] = copy
            copy.neighbors = [deepcopy(neighbor) for neighbor in node.neighbors]
            return copy

        return deepcopy(node)

