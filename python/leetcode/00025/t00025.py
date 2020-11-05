try:
    ListNode
except NameError:
    from list_node import ListNode

from typing import List, Optional


class Group:
    def __init__(self):
        self.size = 0
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None


def get_group(cur: ListNode, k: int):
    group = Group()
    if cur is None:
        return cur, group
    group.tail = group.head = cur
    group.size = 1
    while group.size < k and cur.next is not None:
        cur = cur.next
        group.size += 1
    group.tail = cur
    return cur.next, group


class ResultBuilder:
    def __init__(self):
        self.ptr_to_head = self.tail = ListNode(next=None)

    def add(self, group):
        self.tail.next = group.head
        self.tail = group.tail

    def add_reversed(self, group):
        self.tail.next = group.tail
        self.tail = prev = group.head
        cur = prev.next

        while prev != group.tail:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

    def build(self):
        self.tail.next = None
        return self.ptr_to_head.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        result_builder = ResultBuilder()
        while cur is not None:
            cur, group = get_group(cur, k)
            if group.size == k:
                result_builder.add_reversed(group)
            else:
                result_builder.add(group)

        return result_builder.build()


################################################################


def build_list(lst: List[int]):
    node = None
    for val in lst[::-1]:
        node = ListNode(val, node)
    return node


def recover_array(lst: ListNode) -> list:
    res = []
    while lst is not None:
        res.append(lst.val)
        lst = lst.next
    return res


def test_solution_1():
    lst = build_list([1, 2, 3, 4, 5, 6])
    result = Solution().reverseKGroup(lst, 3)
    assert recover_array(result) == [3, 2, 1, 6, 5, 4]


def test_solution_2():
    lst = build_list([1, 2, 3, 4, 5])
    result = Solution().reverseKGroup(lst, 3)
    assert recover_array(result) == [3, 2, 1, 4, 5]


def test_solution_3():
    lst = build_list([1, 2, 3, 4])
    result = Solution().reverseKGroup(lst, 3)
    assert recover_array(result) == [3, 2, 1, 4]


def test_solution_4():
    lst = build_list([1, 2, 3, 4, 5, 6, 7])
    result = Solution().reverseKGroup(lst, 3)
    assert recover_array(result) == [3, 2, 1, 6, 5, 4, 7]


def test_solution_5():
    lst = build_list([1, 2, 3])
    result = Solution().reverseKGroup(lst, 2)
    assert recover_array(result) == [2, 1, 3]


def test_solution_6():
    lst = build_list([1, 2, 3])
    result = Solution().reverseKGroup(lst, 1)
    assert recover_array(result) == [1, 2, 3]


def test_groups():
    lst = build_list([])
    cur, group = get_group(lst, 3)
    assert group.size == 0
    assert group.head is None
    assert group.tail is None

    lst = build_list([1])
    cur, group = get_group(lst, 3)
    assert group.size == 1
    assert group.head.val == 1
    assert group.tail.val == 1

    lst = build_list([1, 2])
    cur, group = get_group(lst, 3)
    assert group.size == 2
    assert group.head.val == 1
    assert group.tail.val == 2

    lst = build_list([1, 2, 3])
    cur, group = get_group(lst, 3)
    assert group.size == 3
    assert group.head.val == 1
    assert group.tail.val == 3

    lst = build_list([1, 2, 3, 4])
    cur, group = get_group(lst, 3)
    assert group.size == 3
    assert group.head.val == 1
    assert group.tail.val == 3

# if __name__ == '__main__':
#     test_groups()
