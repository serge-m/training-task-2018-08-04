from typing import List

try:
    ListNode()
except NameError:
    from list_node import ListNode


def iter_list(lst: ListNode):
    while lst is not None:
        yield lst.val
        lst = lst.next


def merge2Lists(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if not l1:
        point.next = l2
    else:
        point.next = l1
    return head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            new_lists = [
                merge2Lists(lists[i], lists[i + 1]) for i in range(0, len(lists) - 1, 2)
            ]
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
            lists = new_lists
        return lists[0]


###################################
