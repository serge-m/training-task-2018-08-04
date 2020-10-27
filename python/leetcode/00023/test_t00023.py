import random
from time import time
from typing import List

import numpy as np
from list_node import ListNode
from t00023 import Solution, ListMaker
# from t00023_recursive import Solution


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
        for _ in range(1000)
    ]

    times = []
    for i in range(3):
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
