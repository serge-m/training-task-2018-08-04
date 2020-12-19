import heapq
import math
import sys
from collections import defaultdict
from typing import List, Dict

int_inf = sys.maxsize


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = fill_adj_list(edges, succProb)
        best_paths = {u: int_inf for u in adj_list.keys()}
        q = []
        fill_initial(q, start, best_paths)
        while not empty(q):
            (dist, u) = get_min(q)
            if u == end:
                return distance_to_proba(best_paths[u])
            update_paths(u, adj_list, best_paths, q)

        return 0.0


def update_paths(u, adj_list, best_paths, q):
    for (v, dist) in adj_list[u].items():
        new_dist = best_paths[u] + dist
        if new_dist < best_paths[v]:
            best_paths[v] = new_dist
            heapq.heappush(q, (new_dist, v))


def get_min(q):
    return heapq.heappop(q)


def empty(q):
    return not bool(q)


def proba_to_distance(p):
    return -math.log(p)


def distance_to_proba(d):
    return math.exp(-d)


def fill_initial(q, start, best_paths):
    q.append((proba_to_distance(1.), start))
    best_paths[start] = proba_to_distance(1.)


def fill_adj_list(edges, succProb) -> Dict[int, Dict[int, float]]:
    adj_list = defaultdict(defaultdict)
    for i, ((u, v), prob) in enumerate(zip(edges, succProb)):
        if prob == 0.:
            continue
        dist = proba_to_distance(prob)
        adj_list[u][v] = dist
        adj_list[v][u] = dist
    return adj_list


def test_sol1():
    from pytest import approx
    assert Solution().maxProbability(
        3,
        [[0, 1], [1, 2], [0, 2]],
        [0.5, 0.5, 0.2],
        0,
        2,
    ) == approx(0.25)
