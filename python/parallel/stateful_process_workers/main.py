import time

import numpy as np

from controllers.parallel_pipe_controller import ParallelPipeController
from controllers.sequential_controller import Controller


def execute_test(controller):
    num_frames = 10
    t = time.time()
    for i in range(num_frames):
        frame = np.empty((100, 100), dtype='uint8')
        controller(frame)
    controller.finish()
    t = time.time() - t
    print(f"FPS: {num_frames / t}")
    return t


def main():
    print("sequential")
    execute_test(Controller())
    print("parallel")
    execute_test(ParallelPipeController())


if __name__ == '__main__':
    main()
