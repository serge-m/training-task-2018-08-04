import sys
from typing import List
import bisect


def solve(maxTravelDist, forwardRouteList, returnRouteList) -> List[List]:
    rrs = [
        (rr_cost, rr_id)
        for rr_id, rr_cost in returnRouteList
    ]
    rrs.sort()
    best_val = 0
    best_pairs = []
    for fr_id, fr_cost in forwardRouteList:
        beggest_rr_cost = maxTravelDist - fr_cost
        idx = bisect.bisect_right(rrs, (beggest_rr_cost, sys.maxsize))
        idx -= 1
        while idx >= 0:
            rr_cost, rr_id = rrs[idx]
            if best_val < rr_cost + fr_cost:
                best_val = rr_cost + fr_cost
                best_pairs = [[fr_id, rr_id]]
            elif best_val == rr_cost + fr_cost:
                best_pairs.append([fr_id, rr_id])
            else:
                break
            idx -= 1

    if not best_pairs:
        return [[]]
    else:
        return best_pairs


def test_1():
    maxTravelDist = 7000
    forwardRouteList = [[1, 2000], [2, 4000], [3, 6000]]
    returnRouteList = [[1, 2000]]
    assert solve(maxTravelDist, forwardRouteList, returnRouteList) == [[2, 1]]


def test_2():
    maxTravelDist = 10000
    forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
    returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
    assert solve(maxTravelDist, forwardRouteList, returnRouteList) == [[2, 4], [3, 2]]
