# Investigating on Quicksort corner cases and complexity


In order to understand how quicksort with Hoare partition behaves I made several tests.

Pivot is selected either as the low element `pivot = A[lo]` or as a middle element `pivot = A[(lo+hi) // 2]`:

Mid element is considerably faster on average. In the worst case they are the same. Just the worst case for the

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
