#!/bin/python3

import os
import heapq


def runningMedian(a):
    result = []
    low = []  # heap of pairs (-x, x). highest x is on top
    high = []  # heap of pairs (x, x). lowest x is on top
    for x in a:
        if not low or x <= low[0][1]:
            heapq.heappush(low, (-x, x))
        else:
            heapq.heappush(high, (x, x))

        if len(low) > len(high) + 1:
            (_, v) = heapq.heappop(low)
            heapq.heappush(high, (v, v))
        elif len(high) > len(low):
            (_, v) = heapq.heappop(high)
            heapq.heappush(low, (-v, v))

        if len(low) == len(high):
            med = (low[0][1] + high[0][1]) / 2.
        else:
            med = low[0][1]

        result.append(f"{med:.1f}")

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
