#!/usr/bin/env python
"""
Let's figure out with an example whether it makes sense to use tuples instead of
data classes in parallel processing.
We create list of objects containing  two numpy arrays and one integer in it.
Let's say there is some CPU consuming function that takes those objects and converts
it to a result entry. Result entry consists of one numpy array and a float.
The entries will be implemented as tuple and as data class.

We test it in a multiprocessing environment.

Let's see how much do we pay for having named entities in a class
compared to unnamed entities in tuples.

Sample results:

1)
    data class, multiprocessing, chunk size = 1: 9.559658765792847 sec
    data class, multiprocessing, chunk size = 20: 5.729766607284546 sec
    data class, single process: 19.416381359100342 sec
    tuple, multiprocessing, chunk size = 1: 8.662716388702393 sec
    tuple, multiprocessing, chunk size = 20: 5.679460525512695 sec
    tuple, single process: 19.579129695892334 sec

2)
    data class, multiprocessing, chunk size = 1: 9.396282434463501 sec
    data class, multiprocessing, chunk size = 20: 5.585931062698364 sec
    data class, single process: 19.043205738067627 sec
    tuple, multiprocessing, chunk size = 1: 8.375351190567017 sec
    tuple, multiprocessing, chunk size = 20: 5.288960695266724 sec
    tuple, single process: 19.175997495651245 sec

3)
    data class, multiprocessing, chunk size = 1: 9.289982795715332 sec
    data class, multiprocessing, chunk size = 20: 5.383700609207153 sec
    data class, single process: 19.012136936187744 sec
    tuple, multiprocessing, chunk size = 1: 8.245360612869263 sec
    tuple, multiprocessing, chunk size = 20: 5.601776123046875 sec
    tuple, single process: 19.197880744934082 sec


From those numbers I would conclude that it makes sense to use dataclass
if the operation we perform is significantly slower that object serialization.
With data class we have names for each member of the entity.
That makes code clearer and easier to maintain.
There is very little (if at all) performance benefit in case of proper
settings of parallel processing.


"""
import multiprocessing
from contextlib import contextmanager
from dataclasses import dataclass
from time import time
from typing import Tuple

import numpy as np
import numpy.linalg


@dataclass
class EntityInput:
    coord: np.ndarray
    color: np.ndarray
    label: int


@dataclass
class EntityResult:
    coord: np.ndarray
    distance: float


def slow_operation_on_data_class(inp: EntityInput) -> EntityResult:
    """
    Some dummy operation we want to apply to each entity. Version for data class
    """
    matrix = np.random.random([100, 100])
    for i in range(20):
        matrix = (matrix - 0.5) * matrix
    return EntityResult(coord=inp.coord * 2, distance=np.linalg.norm(inp.coord) + inp.label)


def slow_operation_on_tuple(inp: Tuple[np.ndarray, np.ndarray, int]) -> Tuple[np.ndarray, float]:
    """
    Some dummy operation we want to apply to each entity. Version for tuples.
    """
    matrix = np.random.random([100, 100])
    for i in range(20):
        matrix = (matrix - 0.5) * matrix
    return inp[0] * 2, np.linalg.norm(inp[0]) + inp[2]


@contextmanager
def timer(name):
    t0 = time()
    yield
    t = time() - t0
    print(f"{name}: {t} sec")


if __name__ == '__main__':
    num_objects = 200000

    rs = np.random.RandomState(0)
    tasks_entity = [EntityInput(coord=rs.random([3]), color=rs.random([3]), label=i)
                    for i in range(num_objects)]

    rs = np.random.RandomState(0)
    tasks_tuple = [(rs.random([3]), rs.random([3]), i)
                   for i in range(num_objects)]

    for name, fn, tasks in [
        ("data class", slow_operation_on_data_class, tasks_entity),
        ("tuple", slow_operation_on_tuple, tasks_tuple),
    ]:
        with timer(f"{name}, multiprocessing, chunk size = 1"):
            with multiprocessing.Pool(6) as pool:
                result = list(pool.imap(fn, tasks, chunksize=1))
            assert len(result) == num_objects

        with timer(f"{name}, multiprocessing, chunk size = 20"):
            with multiprocessing.Pool(6) as pool:
                result = list(pool.imap(fn, tasks, chunksize=20))
            assert len(result) == num_objects

        with timer(f"{name}, single process"):
            result = list(map(fn, tasks))
            assert len(result) == num_objects
