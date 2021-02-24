"""
56. Merge Intervals
Medium


with radix sort
104 ms	16.9 MB

O(d*(n+10) + n), d is number of digits in maximum value
"""

from typing import List
import itertools


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = radix_sort(intervals)
        result = []
        for start, end in sorted_intervals:
            if result and result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result


def radix_sort(lst, max_digit_pos=5):
    for i in range(max_digit_pos):
        selector = 10 ** i
        lst = counting_sort(lst, key_fn=(lambda elem: elem[0] // selector % 10), d=10)
        # print(lst)
    return lst


def counting_sort(lst, key_fn, d):
    keys = [key_fn(x) for x in lst]
    # print("counting sort")
    # print(lst)
    # print(keys)
    counts = [0] * d
    for key in keys:
        counts[key] += 1
    if counts[0] == len(lst):  # tiny optimization
        return lst
    starts = list(itertools.accumulate(counts, initial=0))

    result = [None] * len(lst)
    for key, item in zip(keys, lst):
        result[starts[key]] = item
        starts[key] += 1
    return result
