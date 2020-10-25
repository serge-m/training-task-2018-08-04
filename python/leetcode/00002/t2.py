# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1
# None
# 1

# None
# 1
# 1

# 0
# None
# 0


# None
# 0
# 0

# 1
# 2
# 3


def add(current: int, l1: ListNode, l2: ListNode):
    if l1 is None:
        l1, l2 = l2, l1

    if l1 is None:
        if current != 0:
            return ListNode(current, None)
        else:
            return None

    s = current + l1.val
    if l2 is not None:
        s += l2.val
        l2_next = l2.next
    else:
        l2_next = None
    return ListNode(s % 10, add(s // 10, l1.next, l2_next))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return add(0, l1, l2)
