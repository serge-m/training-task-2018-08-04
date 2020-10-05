import multiprocessing
import time
import random
import tqdm


def slow_operation(a):
    """
    Slow operation, return value is not needed in main.
    For example the function opens a file, processes it and dumps the results to a new location.
    """
    time.sleep(random.random())
    return a + 1


def run_operations_in_parallel_without_retrieving_results():
    with  multiprocessing.Pool(6) as pool:
        for _ in tqdm.tqdm(pool.imap_unordered(slow_operation, range(100)), total=100):
            pass


if __name__ == '__main__':
    run_operations_in_parallel_without_retrieving_results()
