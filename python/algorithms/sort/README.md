# Investigating on Quicksort corner cases and complexity


In order to understand how quicksort with Hoare partition behaves I made several tests.

Pivot is selected either as the low element `pivot = A[lo]` or as a middle element `pivot = A[(lo+hi) // 2]`:

Mid element is considerably faster on average. In the worst case they are the same. Just the worst case for the
mid element is a bit different.

### QSortHoarePivotLow
    swaps
    min 0 (0, 1)
    max 1 (1, 0)
    avg 0.5
    cmp
    min 3 (0, 1)
    max 4 (1, 0)
    avg 3.5
    swaps
    min 0 (0, 1, 2)
    max 2 (1, 2, 0)
    avg 1.1666666666666667
    cmp
    min 7 (0, 1, 2)
    max 9 (1, 2, 0)
    avg 8.166666666666666
    swaps
    min 3 (10, 10, 10, 11, 11, 12, 13)
    max 9 (11, 11, 12, 10, 13, 10, 10)
    avg 6.223809523809524
    cmp
    min 27 (11, 10, 10, 11, 10, 12, 13)
    max 38 (13, 10, 10, 10, 11, 11, 12)
    avg 31.72142857142857
    swaps
    min 0 (100, 101, 102, 103, 104, 105, 106, 107, 108)
    max 13 (104, 105, 108, 107, 101, 100, 103, 102, 106)
    avg 7.359071869488536
    cmp
    min 40 (103, 101, 102, 106, 104, 105, 100, 107, 108)
    max 60 (101, 102, 103, 104, 105, 106, 107, 108, 100)
    avg 47.5182208994709

### QSortHoarePivotMid

    swaps
    min 0 (0, 1)
    max 1 (1, 0)
    avg 0.5
    cmp
    min 3 (0, 1)
    max 4 (1, 0)
    avg 3.5
    swaps
    min 0 (0, 1, 2)
    max 2 (1, 2, 0)
    avg 1.1666666666666667
    cmp
    min 7 (0, 1, 2)
    max 9 (1, 2, 0)
    avg 8.0
    swaps
    min 3 (10, 10, 10, 11, 11, 12, 13)
    max 8 (10, 11, 10, 12, 13, 11, 10)
    avg 6.014285714285714
    cmp
    min 27 (10, 10, 11, 11, 10, 12, 13)
    max 37 (10, 10, 12, 13, 11, 11, 10)
    avg 30.814285714285713
    swaps
    min 0 (100, 101, 102, 103, 104, 105, 106, 107, 108)
    max 11 (101, 102, 104, 107, 106, 108, 103, 100, 105)
    avg 6.632275132275132
    cmp
    min 37 (100, 101, 102, 103, 104, 105, 106, 107, 108)
    max 60 (101, 102, 103, 105, 100, 108, 104, 106, 107)
    avg 44.66779100529101

### QSortHoarePivotMidSwapLow

    swaps
    min 1 (0, 1)
    max 2 (1, 0)
    avg 1.5
    cmp
    min 3 (0, 1)
    max 4 (1, 0)
    avg 3.5
    swaps
    min 2 (1, 0, 2)
    max 4 (0, 2, 1)
    avg 3.1666666666666665
    cmp
    min 7 (1, 0, 2)
    max 9 (0, 2, 1)
    avg 8.166666666666666
    swaps
    min 9 (11, 10, 10, 11, 12, 10, 13)
    max 15 (10, 11, 13, 11, 12, 10, 10)
    avg 12.192857142857143
    cmp
    min 27 (11, 10, 10, 11, 12, 10, 13)
    max 38 (10, 10, 12, 13, 11, 10, 11)
    avg 31.745238095238093
    swaps
    min 8 (101, 105, 103, 107, 100, 102, 104, 106, 108)
    max 21 (101, 105, 106, 108, 104, 100, 107, 102, 103)
    avg 15.307098765432098
    cmp
    min 40 (100, 102, 105, 103, 104, 107, 106, 101, 108)
    max 60 (100, 101, 105, 107, 108, 103, 104, 102, 106)
    avg 47.535493827160494

### QSortHoarePivotHiSwapLow

    swaps
    min 1 (1, 0)
    max 2 (0, 1)
    avg 1.5
    cmp
    min 3 (1, 0)
    max 4 (0, 1)
    avg 3.5
    swaps
    min 2 (1, 2, 0)
    max 4 (0, 1, 2)
    avg 3.1666666666666665
    cmp
    min 7 (1, 2, 0)
    max 9 (0, 1, 2)
    avg 8.166666666666666
    swaps
    min 9 (10, 10, 11, 11, 12, 13, 10)
    max 14 (10, 11, 12, 10, 10, 11, 13)
    avg 11.773809523809524
    cmp
    min 28 (10, 10, 12, 10, 11, 13, 11)
    max 37 (10, 10, 10, 11, 11, 12, 13)
    avg 31.604761904761904
    swaps
    min 8 (101, 102, 103, 104, 105, 106, 107, 108, 100)
    max 20 (106, 105, 108, 107, 101, 100, 103, 102, 104)
    avg 14.524118165784833
    cmp
    min 40 (101, 100, 103, 104, 102, 106, 107, 108, 105)
    max 60 (100, 101, 102, 103, 104, 105, 106, 107, 108)
    avg 47.00933090828924



# References

* Wiki https://en.wikipedia.org/wiki/Quicksort
* about pivot choice:
  * https://cs.stackexchange.com/questions/97727/hoare-partitioning-scheme-in-quicksort
* explanation about lomuto vs hoare schemes on reddit: [hoares_partition_scheme_fails_for_this_input](https://www.reddit.com/r/AskProgramming/comments/6emoyb/hoares_partition_scheme_fails_for_this_input/dicihap?utm_source=share&utm_medium=web2x&context=3)
* about many things in qsort: [combsortcs2p-and-other-sorting-algorithms](https://code.google.com/archive/p/combsortcs2p-and-other-sorting-algorithms/wikis/QuickSort.wiki)
  (including a note about tail recursion).


