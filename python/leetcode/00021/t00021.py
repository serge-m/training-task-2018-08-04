"""
21. Merge Two Sorted Lists
Easy
t = 10

"""

# Definition for singly-linked list.
try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        to_head = ListNode()
        tail = to_head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if l1 is not None:
            tail.next = l1
        else:
            tail.next = l2

        return to_head.next


"""

1 2 4
1 3 4

                                 t
to_head: 0, 1, 1(l1) 3(l2) 3(l1) 4(l2) 4(l1) None

l1 = 4
l2 = None




"""
