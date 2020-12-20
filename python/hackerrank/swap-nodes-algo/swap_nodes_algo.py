#!/bin/python3

import os
import sys


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    tree = indexes
    return [list(traverse_and_swap(tree, 1, query, 1)) for query in queries]


def traverse_and_swap(tree, cur, query, depth):
    if cur == -1:
        return
    if depth > query:
        depth = depth - query
    node = tree[cur - 1]
    if depth == query:
        node[:] = node[::-1]
    for val in traverse_and_swap(tree, node[0], query, depth + 1):
        yield val
    yield cur
    for val in traverse_and_swap(tree, node[1], query, depth + 1):
        yield val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
