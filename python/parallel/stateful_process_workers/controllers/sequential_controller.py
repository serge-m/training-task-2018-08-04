from components.components import Detector, Processor, _compute_size, _obj_to_class, Aggregator


class Controller:
    def __init__(self):
        self.detector = Detector()
        self.size_estimator = Processor(fn=_compute_size)
        self.classifier = Processor(fn=_obj_to_class)
        self.aggregator = Aggregator()
        self.stats = []

    def __call__(self, frame):
        objects = self.detector(frame)
        sizes = self.size_estimator(objects)
        classes = self.classifier(objects)
        stat = self.aggregator(sizes, classes)
        self.stats.append(stat)

    def finish(self):
        pass
