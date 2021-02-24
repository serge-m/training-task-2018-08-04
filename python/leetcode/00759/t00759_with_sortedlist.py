"""
759. Employee Free Time
Hard


for each interval we do logarithmic operations of bisect and add.
also we are deleting intervals of free time. -> O(n log n)
Amount of intervals of free time is proportional to the amount of work intervals in
the worst case. We do each delete at most once -> O(log n) for each deletion. In total deletion:
O(n log n)
Iteration in the end: O(n log n)
Total O(n log n)

212 ms	16.6 MB

"""

from sortedcontainers import SortedList

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
        free_time = SortedList([-1, 10 ** 9])
        for s in schedule:
            for i in s:
                p_s = free_time.bisect_left(i.start)
                p_e = free_time.bisect_left(i.end)
                if p_e == 0 or p_s == len(free_time):
                    continue
                del free_time[p_s:p_e]
                if p_s % 2 == 1:
                    free_time.add(i.start)
                if p_e % 2 == 1:
                    free_time.add(i.end)

        return [
            Interval(free_time[i], free_time[i + 1])
            for i in range(2, len(free_time) - 2, 2)
            if free_time[i] < free_time[i + 1]
        ]




