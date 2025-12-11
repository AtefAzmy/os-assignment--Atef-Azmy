# semaphore.py
# Demonstrates using a Semaphore to limit concurrent access (e.g., a pool of resources).

import threading, time, random

semaphore = threading.Semaphore(3)  # allow up to 3 concurrent workers

def worker(i):
    print(f'Worker-{i} waiting to enter critical section')
    with semaphore:
        print(f'Worker-{i} entered (allowed).')
        # simulate work with variable time
        time.sleep(random.uniform(0.5, 1.5))
        print(f'Worker-{i} leaving.')

def main():
    print('--- Semaphore demo ---')
    threads = []
    for i in range(8):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('All workers finished.')

if __name__ == '__main__':
    main()
