# 两个线程交替打印

import threading
import time

def a():
    while True:
        lockb.acquire()
        print('字节跳动2019 a')
        locka.release()
        time.sleep(0.5)


def b():
    while True:
        locka.acquire()
        print('字节跳动2019 b')
        lockb.release()
        time.sleep(0.5)


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()

    ta = threading.Thread(None, a)
    tb = threading.Thread(None, b)

    locka.acquire()     #保证a先执行

    ta.start()
    tb.start()