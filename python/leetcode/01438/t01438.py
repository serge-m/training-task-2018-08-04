"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
"""
# from dataclasses import dataclass
from typing import List

from sortedcontainers import SortedList, SortedDict


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

        w = SortedDict()
        start = 0
        end = 0

        def add(value):
            if value not in w:
                w[value] = 0
            w[value] += 1

        def delete(value):
            if w[value] == 1:
                del w[value]
            else:
                w[value] -= 1

        while end < n:

            add(nums[end])
            largest = w.peekitem(index=-1)
            smallest = w.peekitem(index=0)
            if largest[0] - smallest[0] > limit:
                delete(nums[start])
                start += 1
            end += 1
        return end - start

