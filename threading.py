# threading.py
# Demonstrates basic threading in Python: multiple threads incrementing a shared counter.
# Includes an example with and without a Lock to show race conditions.

import threading
import time

counter = 0

def worker_no_lock(n, name):
    global counter
    for _ in range(n):
        # race condition possible here
        counter += 1
        time.sleep(0.0001)
    print(f"{name} finished (no lock)")

def worker_with_lock(n, lock, name):
    global counter
    for _ in range(n):
        with lock:
            counter += 1
        time.sleep(0.0001)
    print(f"{name} finished (with lock)")

def main():
    global counter
    print('--- Threading demo ---')

    # Demo 1: without lock (race condition expected)
    counter = 0
    t1 = threading.Thread(target=worker_no_lock, args=(1000, 'T1'))
    t2 = threading.Thread(target=worker_no_lock, args=(1000, 'T2'))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print('Expected counter 2000, got (no lock):', counter)

    # Demo 2: with Lock (safe)
    counter = 0
    lock = threading.Lock()
    t3 = threading.Thread(target=worker_with_lock, args=(1000, lock, 'T3'))
    t4 = threading.Thread(target=worker_with_lock, args=(1000, lock, 'T4'))
    t3.start(); t4.start()
    t3.join(); t4.join()
    print('Expected counter 2000, got (with lock):', counter)

if __name__ == '__main__':
    main()
