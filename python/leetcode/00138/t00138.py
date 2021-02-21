"""
138. Copy List with Random Pointer
Medium
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cur = head
        while cur is not None:
            copy_cur = Node(cur.val, cur.next, cur.random)
            cur.next = copy_cur
            cur = copy_cur.next

        copy_head = head.next

        cur = head
        while cur is not None:
            copy_cur = cur.next
            copy_cur.random = cur.random.next if cur.random is not None else None
            cur = copy_cur.next

        cur = head
        while cur is not None:
            copy_cur = cur.next
            cur.next = copy_cur.next
            if cur.next is not None:
                copy_cur.next = cur.next.next
            cur = cur.next
        return copy_head


"""

7   13  11  10  1
v   v   v   v   v 
7   13

"""
