"""
729. My Calendar I
Medium

segment intersection
"""

from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.a = SortedList()

    def book(self, start: int, end: int) -> bool:
        seg = (start, end)
        pos = self.a.bisect_left(seg)
        if pos < len(self.a):
            if self.a[pos][0] < end:
                return False
        if pos > 0:
            if self.a[pos - 1][1] > start:
                return False
        self.a.add(seg)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
