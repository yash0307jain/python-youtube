"""
`Multiprocessing` → Multiple processes with separate memory (parallelism).
"""

# =======================================================
# 1. Multiprocessing (No GIL limitation)
# =======================================================
# import time
# from multiprocessing import Process


# def count_down(n):
#     while n > 0:
#         n -= 1


# if __name__ == "__main__":
#     start = time.time()

#     # Create multiple processes
#     p1 = Process(target=count_down, args=(10_000_000,))
#     p2 = Process(target=count_down, args=(10_000_000,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(f"Processes total time: {time.time() - start:.2f} seconds")


# =======================================================
# 2. Multiprocessing with Pool and map()
# =======================================================

# import time
# from multiprocessing import Pool


# def square(n):
#     time.sleep(1)
#     return n * n


# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5] * 10
#     start = time.time()

#     with Pool(processes=5) as pool:
#         results = pool.map(square, numbers)

#     print("Results:", results)
#     print(f"Time taken: {time.time() - start:.2f} seconds")


# =======================================================
# 3. Multiprocessing with Queue (Data Exchange)
# =======================================================

# from multiprocessing import Process, Queue


# def worker(q: Queue, num: int):
#     q.put(f"Data sent from child process, {num}")


# if __name__ == "__main__":
#     queue = Queue()

#     processes: list[Process] = []
#     for i in range(2):
#         process = Process(
#             target=worker,
#             args=(
#                 queue,
#                 i + 1,
#             ),
#         )
#         processes.append(process)
#         process.start()

#     for process in processes:
#         print(queue.get())  # Receive data from child
#         process.join()


# =======================================================
# 4. Multithreading vs Multiprocessing
# =======================================================
import time
from multiprocessing import Process
from threading import Thread


def work(duration):
    print(f"Working for {duration}s...")
    time.sleep(duration)
    print(f"Done after {duration}s")


def run_threads():
    threads = []
    numbers = [1, 2, 3] * 10
    for i in numbers:
        t = Thread(target=work, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def run_processes():
    processes = []
    numbers = [1, 2, 3] * 10
    for i in numbers:
        p = Process(target=work, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    print("Threading demo:")
    t1 = time.time()
    run_threads()
    print("Total Time (Threads):", time.time() - t1)

    print("\nMultiprocessing demo:")
    t2 = time.time()
    run_processes()
    print("Total Time (Processes):", time.time() - t2)
