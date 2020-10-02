import traceback
from multiprocessing import Process, Pipe
from typing import Callable

from components.components import Detector, Processor, Aggregator, _compute_size, _obj_to_class


def pipe_worker(pipe, factory: Callable):
    try:
        print("worker started")
        processor = factory()
        while True:
            msg = pipe.recv()
            if msg is None:
                break
            result = processor(msg)
            pipe.send(result)
        print("worker exited correctly")
    except Exception:
        print("An exception occurred. We notify the main process by closing our end of the pipe."
              "It would be nicer to send some info to the main process.")
        traceback.print_exc()
        pipe.close()


class ParallelPipeController:
    def __init__(self, size_estimator_factory=lambda: Processor(fn=_compute_size)):
        self.pipe_size_estimator, pipe_size_worker = Pipe()

        self.detector = Detector()
        self.size_estimator = Process(
            target=pipe_worker,
            args=(pipe_size_worker, size_estimator_factory),
            daemon=True
        )
        self.classifier = Processor(fn=_obj_to_class)
        self.aggregator = Aggregator()
        self.stats = []
        self.size_estimator.start()

    def __call__(self, frame):
        objects = self.detector(frame)
        self.pipe_size_estimator.send(objects)
        classes = self.classifier(objects)
        try:
            sizes = self.pipe_size_estimator.recv()
        except EOFError as e:
            raise RuntimeError("Unable to get data from process. Probably exception occurred") from e
        stat = self.aggregator(sizes, classes)
        self.stats.append(stat)

    def finish(self):
        self.pipe_size_estimator.send(None)
        self.size_estimator.join()
