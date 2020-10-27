import heapq
import random
from dataclasses import dataclass, field
from time import time
from typing import List, Any
import queue


import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


@dataclass(order=True)
class PQItem:
    priority: int
    entry: Any = field(compare=False)


class PriorityQueue:
    def __init__(self):
        self._pq = queue.PriorityQueue()

    def push(self, priority, index):
        self._pq.put((priority, index))

    def empty(self) -> bool:
        return self._pq.empty()

    def pop(self):
        return self._pq.get()


###################################


def build_list(lst: List[int]):
    node = None
    for val in lst[::-1]:
        node = ListNode(val, node)
    return node


def recover_list(lst: ListNode):
    res = []
    while lst is not None:
        res.append(lst.val)
        lst = lst.next
    return res


def test_solution1():
    # rs = random.Random(0)
    # a, b, c = [
    #     sorted([rs.randint(0, 20) for _ in range(l)])
    #     for l in [5, 2, 3]
    # ]
    a = [1, 8, 12, 13, 16]
    b = [12, 15]
    c = [9, 11, 15]

    res = Solution().mergeKLists([build_list(l) for l in [a, b, c]])
    assert recover_list(res) == sorted(a + b + c)


def test_solution_speed():
    rs = random.Random(0)
    arrays = [
        sorted([rs.randint(0, 10000) for _ in range(rs.randint(400, 500))])
        for _ in range(100)
    ]


    times = []
    for i in range(10):
        lists = [build_list(arr) for arr in arrays]
        t = time()
        res = Solution().mergeKLists(lists)
        times.append(time() - t)

    times = np.array(times)
    print(f"elapsed min {times.min()} mean {times.mean()}, std {times.std()}")
    assert recover_list(res) == sorted(sum(arrays, []))


def test_list_maker():
    lm = ListMaker()
    assert recover_list(lm.add(1).add(2).build()) == [1, 2]
    lm = ListMaker()
    assert recover_list(lm.add(1).add(2).add(100).build()) == [1, 2, 100]


def test_list_maker_2():
    lm = ListMaker()
    assert recover_list(lm.add(1).build()) == [1]


def test_list_maker_empty():
    lm = ListMaker()
    assert recover_list(lm.build()) == []
