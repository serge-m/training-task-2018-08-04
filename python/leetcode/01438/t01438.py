"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
"""
# from dataclasses import dataclass
from typing import List

from sortedcontainers import SortedList


# @dataclass
# class Node:
#     val: int = 0
#     cnt: int = 0
#     left: Node = None
#     right: Node = None


# class Tree:
#     def __init__(self,):
#         self.root = None
#         self.min = None
#         self.max = None

#     def add(self, val):
#         if self.root is None:
#             self.root = Node(val, 1)
#             self.min = val
#             self.max = val
#             return
#         add(self.root, val)
#         self.min = min(self.min, val)
#         self.max = max(self.max, val)

#     def remove(self, val):
#         if self.root is None:
#             raise RuntimeError("empty")
#         self.root = remove(self.root, val)

# def remove(node, val):


# def add(node, val):
#     if node.val == val:
#         node.cnt += 1
#         return
#     elif val < node.val:
#         if node.left is None:
#             node.left = Node(val, 1)
#         else:
#             add(node.left, val)
#     else:
#         if node.right is None:
#             node.right = Node(val, 1)
#         else:
#             add(node.right, val)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        w = SortedList()
        start = 0
        end = 0
        while end < n:
            w.add(nums[end])
            if w[-1] - w[0] > limit:
                w.remove(nums[start])
                start += 1
            end += 1
        return end - start
