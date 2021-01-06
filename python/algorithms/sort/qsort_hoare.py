import itertools
from abc import ABCMeta, abstractmethod
from statistics import mean

import pytest


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


class CallCount:
    def __init__(self, fn):
        self.cnt = 0
        self._fn = fn

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self._fn(*args, **kwargs)


class QSort(metaclass=ABCMeta):
    def __init__(self, swap, predicate):
        self.swap = swap
        self.predicate = predicate

    def sort(self, a):
        self.sort_range(a, 0, len(a) - 1)

    def sort_range(self, a, lo, hi):
        if lo < hi:
            pivot = self.pivot(a, lo, hi)
            p = self.partition(a, lo, hi, pivot)
            self.sort_range(a, lo, p)
            self.sort_range(a, p + 1, hi)

    @abstractmethod
    def partition(self, a, lo, hi, pivot):
        pass

    @abstractmethod
    def pivot(self, a, lo, hi):
        pass


class QSortHoare(QSort):
    def partition(self, a, lo, hi, pivot):
        i = lo - 1
        j = hi + 1
        while True:
            while True:
                i += 1
                if not self.predicate(a[i], pivot):
                    break

            while True:
                j -= 1
                if not self.predicate(pivot, a[j]):
                    break

            if i >= j:
                return j

            self.swap(a, i, j)


class QSortHoarePivotLow(QSortHoare):
    # noinspection PyMethodMayBeStatic
    def pivot(self, a, lo, hi):
        return a[lo]


class QSortHoarePivotHigh(QSortHoare):
    # noinspection PyMethodMayBeStatic
    def pivot(self, a, lo, hi):
        return a[hi]


class QSortHoarePivotMid(QSortHoare):
    # noinspection PyMethodMayBeStatic
    def pivot(self, a, lo, hi):
        return a[(lo + hi) // 2]


class QSortHoarePivotMidSwapLow(QSortHoare):
    # noinspection PyMethodMayBeStatic
    def pivot(self, a, lo, hi):
        self.swap(a, lo, (lo + hi) // 2)
        return a[lo]


class QSortHoarePivotHiSwapLow(QSortHoare):
    # noinspection PyMethodMayBeStatic
    def pivot(self, a, lo, hi):
        self.swap(a, lo, hi)
        return a[lo]


def run_counting(sort_cls, arr, sorted_validation=None):
    swap_cnt = CallCount(swap)
    predicate_cnt = CallCount(lambda x, y: x < y)
    q = sort_cls(swap=swap_cnt, predicate=predicate_cnt)
    a_copy = list(arr)
    q.sort(a_copy)
    if sorted_validation is not None:
        assert sorted_validation == a_copy
    return predicate_cnt.cnt, swap_cnt.cnt


class MinMaxStat:
    def __init__(self):
        self.min = None
        self.min_item = None
        self.max = None
        self.max_item = None
        self.sum = 0
        self.cnt = 0

    def update(self, value, item):
        self.sum += value
        self.cnt += 1

        if self.min is None or self.min > value:
            self.min = value
            self.min_item = item

        if self.max is None or self.max < value:
            self.max = value
            self.max_item = item

    def str(self):
        return f"min {self.min} {self.min_item}\nmax {self.max} {self.max_item}\navg {self.sum / self.cnt}"


def test_hoare():
    arrays = [
        [0, 1],
        [0, 1, 2],
        [10, 10, 10, 11, 11, 12, 13],
        list(range(100, 109)),
    ]
    for sort_cls in [QSortHoarePivotLow, QSortHoarePivotMid, QSortHoarePivotMidSwapLow, QSortHoarePivotHiSwapLow]:
        print(sort_cls.__name__)
        for arr in arrays:
            swapstat = MinMaxStat()
            cmpstat = MinMaxStat()
            sorted_arr = sorted(arr)
            for p in itertools.permutations(sorted_arr):
                predicate_cnt, swap_cnt = run_counting(sort_cls, p, sorted_arr)
                swapstat.update(swap_cnt, p)
                cmpstat.update(predicate_cnt, p)
                # print(f"{swap_cnt.cnt:5d} {predicate_cnt.cnt:5d} {p}")

            print(f"swaps\n{swapstat.str()}")
            print(f"cmp\n{cmpstat.str()}")


def test_worst_case_hoare_low():
    run_counting(QSortHoarePivotLow, [13, 10, 10, 10, 11, 11, 12])


def test_hoare_low__many_comparisons_sorted():
    res = run_counting(QSortHoarePivotLow, (100, 101, 102, 103, 104, 105, 106, 107, 108))
    print(res)


def test_hoare_low__worst_case__almost_sorted():
    res = run_counting(QSortHoarePivotLow, (101, 102, 103, 104, 105, 106, 107, 108, 100))
    print(res)


def test_hoare_high_failing():
    with pytest.raises(RecursionError):
        run_counting(QSortHoarePivotHigh, [0, 1])


def test_hoare_high_failing2():
    with pytest.raises(RecursionError):
        run_counting(QSortHoarePivotHigh, [1, 0, 2])
