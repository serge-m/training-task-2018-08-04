"""
759. Employee Free Time
Hard

O(n^2)
iterative, linear merging on two schedules

"""

# Definition for an Interval.
try:
    Interval
except NameError:
    class Interval:
        def __init__(self, start: int = None, end: int = None):
            self.start = start
            self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # m1 = merge_schedule([Interval(1, 3), Interval(6,7)], [Interval(2,5), Interval(9, 12)])
        # print(str_s(m1))
        n = len(schedule)
        all_work = schedule[0]
        for i in range(1, n):
            all_work = merge_schedule(all_work, schedule[i])

        return free_from_work(all_work)


def str_s(s):
    return ", ".join([f"[{seg.start}, {seg.end}]" for seg in s])


class Itr:
    def __init__(self, s):
        self.i = 0
        self.s = s

    def next(self):
        if self.i < len(self.s):
            self.i += 1

    def __getitem__(self, idx):
        if self.i + idx < len(self.s):
            return self.s[self.i + idx]
        else:
            return None


def merge_schedule(s1, s2):
    result = []
    i1 = Itr(s1)
    i2 = Itr(s2)
    while True:
        # print("result", str_s(result))
        # print("i1", (i1[0].start, i1[0].end) if i1[0] else None)
        # print("i2", (i2[0].start, i2[0].end) if i2[0] else None)
        if i1[0] is None or (i2[0] is not None and i1[0].start > i2[0].start):
            i1, i2 = i2, i1
        cur = i1[0]
        if cur is None:
            break
        # print("cur", (cur.start, cur.end) if cur else None)
        if result and result[-1].end >= cur.start:
            last = result[-1]
            last.start, last.end = min(last.start, cur.start), max(last.end, cur.end)
        else:
            result.append(cur)
        i1.next()
    return result


def merge_schedule_v1(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    i1 = 0
    i2 = 0
    result = []
    while i1 < n1 or i2 < n2:
        x1 = s1[i1] if i1 < n1 else None
        x2 = s2[i2] if i2 < n2 else None
        if result:
            last = result[-1]
            if x1 is not None and last.end <= x1.start:
                last.start, last.end = min(last.start, x1.start), max(last.end, x1.end)
                i1 += 1
                continue
            if x2 is not None and last.end <= x2.start:
                last.start, last.end = min(last.start, x2.start), max(last.end, x2.end)
                i2 += 1
                continue
        # no intersection with last result
        if x1 is None:
            result.append(x2)
            i2 += 1
            continue
        if x2 is None:
            result.append(x1)
            i1 += 1
            continue

        if x1.start < x2.start:
            result.append(x1)
            i1 += 1
        else:
            result.append(x2)
            i2 += 1

    return result


def free_from_work(work):
    return [
        Interval(work[i].end, work[i + 1].start)
        for i in range(len(work) - 1)
    ]


