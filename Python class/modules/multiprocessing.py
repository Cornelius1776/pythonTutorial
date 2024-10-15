# This is when tasks run on parallel cpu cores. Multiprocessing is best for CPU intensive tasks.
# NOTE: multithreading runs concurrently, multiprocessing runs in parallel

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    x = Process(target=counter, args=(10000000000,))
    x.start()
    x.join()
    print(f"Finshed in {time.perf_counter()} seconds")


if __name__ == "__main__":
    main()
