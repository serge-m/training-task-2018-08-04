"""
759. Employee Free Time
Hard

sort everything, merge iteratively
	76 ms	16.5 MB
O(n + n log n)
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
        schedule = sorted(sum(schedule, []), key=lambda interv: interv.start)
        n = len(schedule)
        all_work = merge_schedule(schedule)
        return free_from_work(all_work)


def str_s(s):
    return ", ".join([f"[{seg.start}, {seg.end}]" for seg in s])


def merge_schedule(s):
    result = []
    for cur in s:
        if result and result[-1].end >= cur.start:
            last = result[-1]
            last.end = max(last.end, cur.end)
        else:
            result.append(cur)
    return result


def free_from_work(work):
    return [
        Interval(work[i].end, work[i + 1].start)
        for i in range(len(work) - 1)
    ]


