#!/bin/python3

import os
import sys


#
# Complete the runningMedian function below.
#
def median(a):
    m = len(a) // 2
    if len(a) % 2 == 1:
        return a[m]
    else:
        return (a[m - 1] + a[m]) / 2


def runningMedian(a):
    result = []
    cur = []
    for x in a:
        cur.append(x)
        cur.sort()
        result.append(f"{median(cur):.1f}")

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
