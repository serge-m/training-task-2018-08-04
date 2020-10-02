from typing import List, Tuple

import numpy as np


class Detector:
    def __call__(self, frame: np.ndarray) -> List:
        return [
            np.array([x, 100 - x, x, x, x]) for x in range(0, 50)
        ]


class Processor:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, objects: List[np.ndarray]) -> List:
        return [self.fn(obj) for obj in objects]


class FailingProcessor(Processor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cnt_calls = 0

    def __call__(self, *args, **kwargs) -> List:
        if self.cnt_calls > -1:
            raise RuntimeError("Some fake error")
        self.cnt_calls += 1
        return super().__call__(*args, **kwargs)


def _compute_size(obj):
    """
    Some slow processing
    """
    x, y = obj[:2]
    res = 0
    for i in range(10000 + x):
        res = res // 20 + (i + x)
    return res


def _obj_to_class(obj) -> int:
    """
    Some slow processing
    """
    x, y = obj[:2]
    res = 0
    for i in range(10000 + y):
        res = res // 20 + (i + x**2)
    return res % 4


class Aggregator:
    def __init__(self, num_classes=4):
        self.num_classes = num_classes

    def __call__(self, sizes: List[int], classes: List[int]) -> Tuple[int, int]:
        return np.max(sizes), np.min(sizes)

    def _obj_to_class(self, obj) -> int:
        x, y = obj
        return x * y / 256 % self.num_classes
