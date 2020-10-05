import multiprocessing
import numpy as np
import tqdm


def slow_operation(a):
    """
    Slow operation, return value is not needed in main.
    For example the function opens a file, processes it and dumps the results to a new location.
    """
    z = np.random.random([1000, 1000])
    for i in range(50):
        z = z * (z - 0.5)
    return z


def parallel_with_imap_unordered():
    with multiprocessing.Pool(6) as pool:
        for _ in tqdm.tqdm(pool.imap_unordered(slow_operation, range(100)), total=100):
            pass
    # we don't need to pool.join() here because imap* waits for all the tasks to complete


def wrong1():
    with multiprocessing.Pool(6) as pool:
        for _ in tqdm.tqdm(pool.map(slow_operation, range(100)), total=100):
            pass


def parallel_with_callback():
    pbar = tqdm.tqdm(total=100)

    def update(*a):
        pbar.update()

    pool = multiprocessing.Pool(6)
    for i in range(pbar.total):
        pool.apply_async(slow_operation, args=(i,), callback=update)
    pool.close()
    # We need `pool.join` to wait for all the processes to finish.
    pool.join()


if __name__ == '__main__':
    # wrong1()
    # parallel_with_imap_unordered()
    parallel_with_callback()
