import math
import sys
from collections import defaultdict
from typing import List, Dict

int_inf = sys.maxsize


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = fill_adj_list(edges, succProb)
        visited = set()
        best_paths = {u: int_inf for u in adj_list.keys()}
        best_paths[start] = proba_to_distance(1.)
        while len(visited) != n:
            (dist, u) = get_min(visited, best_paths)
            if u == end or u == -1:
                if end in best_paths:
                    return distance_to_proba(best_paths[end])
                else:
                    return 0.
            update_paths(u, adj_list, visited, best_paths)

        return 0.0


def update_paths(u, adj_list, visited: set, best_paths):
    for (v, dist) in adj_list[u].items():
        new_dist = best_paths[u] + dist
        if new_dist < best_paths[v]:
            best_paths[v] = new_dist
    visited.add(u)


def get_min(visited, best_paths):
    best_u = -1
    best_dist = int_inf
    for u, dist in best_paths.items():
        if u not in visited and dist < best_dist:
            best_u, best_dist = u, dist
    return best_dist, best_u


def proba_to_distance(p):
    return -math.log(p)


def distance_to_proba(d):
    return math.exp(-d)


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
