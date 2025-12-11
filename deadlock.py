# deadlock.py
# Demonstrates a simple deadlock scenario with two locks acquired in opposite orders.
# WARNING: If you run this code, it may hang because of deadlock. For demonstration only.

import threading, time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    print('Thread-1 trying to acquire lock_a')
    lock_a.acquire()
    print('Thread-1 acquired lock_a')
    time.sleep(0.5)
    print('Thread-1 trying to acquire lock_b')
    lock_b.acquire()
    print('Thread-1 acquired lock_b')
    # release (may never reach here in real deadlock)
    lock_b.release()
    lock_a.release()
    print('Thread-1 finished')

def thread2():
    print('Thread-2 trying to acquire lock_b')
    lock_b.acquire()
    print('Thread-2 acquired lock_b')
    time.sleep(0.5)
    print('Thread-2 trying to acquire lock_a')
    lock_a.acquire()
    print('Thread-2 acquired lock_a')
    lock_a.release()
    lock_b.release()
    print('Thread-2 finished')

def main():
    print('--- Deadlock demo ---')
    t1 = threading.Thread(target=thread1, name='T1')
    t2 = threading.Thread(target=thread2, name='T2')
    t1.start(); t2.start()
    # join with timeout to avoid indefinite hang in environments that run this script
    t1.join(timeout=3)
    t2.join(timeout=3)
    if t1.is_alive() or t2.is_alive():
        print('\nDetected potential deadlock (threads still alive after timeout).')
        print('In a real system this would require deadlock detection or design changes.')
    else:
        print('\nNo deadlock detected (threads finished).')

if __name__ == '__main__':
    main()
