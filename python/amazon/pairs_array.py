"""
Given array or ratios, compute another ratio.

a/b = 5.0, b/c = 7.0, c/d = 2.0.
Query = {a,c} = a/c = a/b * b/c = 5.0 * 7.0 = 35.0


t=20
"""

from collections import defaultdict


def find(pairs, weights, query):
    adj = defaultdict(defaultdict)
    for (start, end), w in zip(pairs, weights):
        adj[start][end] = w
        if w != 0:
            adj[end][start] = 1 / w

    visited = defaultdict(int)
    start, end = query
    return dfs(adj, visited, start, end)


def dfs(adj, visited, start, end):
    visited[start] = 1
    if start == end:
        return 1.

    for u, w in adj[start].items():
        if not visited.get(u):
            p = dfs(adj, visited, u, end)
            if p is not None:
                return p * w

    return None


def test_find():
    a, b, c, d = 'abcd'
    assert find([(a, b), (b, c), (c, d)], [5.0, 7.0, 2.0], (a, c)) == 35


def test_find2():
    a, b, c, d = 'abcd'
    assert find([(a, b), (b, c), (c, d)], [5.0, 7.0, 2.0], (d, a)) == 1 / 70


def test_find3():
    a, b, c, d = 'abcd'
    assert find([(a, b), (b, c), (c, d)], [5.0, 7.0, 2.0], (b, d)) == 14


def test_find4():
    a, b, c, d = 'abcd'
    assert find([(a, b), (b, c), (c, d)], [5.0, 7.0, 2.0], (c, a)) == 1 / 35
