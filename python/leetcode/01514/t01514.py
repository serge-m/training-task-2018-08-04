import heapq
import math
import sys
from typing import List, Tuple

int_inf = sys.maxsize


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = fill_adj_list(n, edges, succProb)
        is_visited = [False for _ in range(n)]
        best_paths = [int_inf for _ in range(n)]
        q = []
        fill_initial(q, start, best_paths)
        while not empty(q):
            (dist, u) = get_min(q)
            if u == end:
                return distance_to_proba(best_paths[u])
            update_paths(u, adj_list, is_visited, best_paths, q)

        return 0.0


def update_paths(u, adj_list, is_visited, best_paths, q):
    if is_visited[u]:
        return
    for (v, dist) in adj_list[u]:
        new_dist = best_paths[u] + dist
        if new_dist < best_paths[v]:
            best_paths[v] = new_dist
            heapq.heappush(q, (new_dist, v))
    is_visited[u] = True


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


def fill_adj_list(n, edges, succProb) -> List[List[Tuple[int, float]]]:
    adj_list = [[] for _ in range(n)]
    for i, ((u, v), prob) in enumerate(zip(edges, succProb)):
        if prob == 0.:
            continue
        dist = proba_to_distance(prob)
        adj_list[u].append((v, dist))
        adj_list[v].append((u, dist))
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
