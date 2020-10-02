

import pytest

from components.components import _compute_size, FailingProcessor
from controllers.parallel_pipe_controller import ParallelPipeController
from controllers.sequential_controller import Controller
from main import execute_test


def test_sequential_controller():
    execute_test(Controller())


def test_parallel_controller():
    execute_test(ParallelPipeController())


def test_exception_in_parallel_controller():
    with pytest.raises(RuntimeError):
        execute_test(ParallelPipeController(size_estimator_factory=lambda: FailingProcessor(fn=_compute_size)))


