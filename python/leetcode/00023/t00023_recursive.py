from typing import List

try:
    ListNode()
except NameError:
    from list_node import ListNode


def iter_list(lst: ListNode):
    while lst is not None:
        yield lst.val
        lst = lst.next


def merge(list1, list2):
    lm = ListMaker()
    if list2 is not None:
        while list1 is not None:
            if list2.val < list1.val:
                list1, list2 = list2, list1
            lm.add(list1.val)
            list1 = list1.next

    for value in iter_list(list1):
        lm.add(value)
    for value in iter_list(list2):
        lm.add(value)

    return lm.build()


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            new_lists = [
                merge(lists[i], lists[i + 1]) for i in range(0, len(lists) - 1, 2)
            ]
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
            lists = new_lists
        return lists[0]


class ListMaker:
    def __init__(self):
        self._init()

    def _init(self):
        self.head = self.tail = ListNode(0)

    def add(self, value):
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        return self

    def build(self):
        return self.head.next

###################################
