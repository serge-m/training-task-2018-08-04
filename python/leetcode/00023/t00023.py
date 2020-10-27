import heapq
from typing import List

try:
    ListNode()
except NameError:
    from list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_maker = ListMaker()
        pq = PriorityQueue()
        for i in range(len(lists)):
            if lists[i] is not None:
                pq.push(lists[i].val, i)
                lists[i] = lists[i].next
        while not pq.empty():
            val, i = pq.pop()
            list_maker.add(val)
            if lists[i] is not None:
                pq.push(lists[i].val, i)
                lists[i] = lists[i].next
        return list_maker.build()


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

class PriorityQueue:
    def __init__(self):
        self._pq = []

    def push(self, priority, index):
        heapq.heappush(self._pq, (priority, index))

    def empty(self) -> bool:
        return not self._pq

    def pop(self):
        return heapq.heappop(self._pq)

###################################
