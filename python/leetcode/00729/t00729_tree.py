"""
729. My Calendar I
Medium

segment intersection
tree
"""


class Node:
    def __init__(self, seg):
        self.seg = seg
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, seg):
        if self.root is None:
            self.root = Node(seg)
            return True
        return insert(self.root, seg)


def insert(root, seg):
    if seg[1] <= root.seg[0]:
        if root.left is None:
            root.left = Node(seg)
            return True
        return insert(root.left, seg)
    if root.seg[1] <= seg[0]:
        if root.right is None:
            root.right = Node(seg)
            return True
        return insert(root.right, seg)
    # default case: intersection
    return False


class MyCalendar:

    def __init__(self):
        self.tree = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.tree.insert((start, end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
