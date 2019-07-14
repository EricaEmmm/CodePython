# 创建多个生产者和消费者，并且加上条件锁，避免线程冲突

import threading
from threading import Thread
from threading import Condition, Lock

import time
import random


c = Condition()     # 条件锁  Lock()#
itemNum = 0
item = 0

# 消费者
def consumer():
    global item     # 商品编号
    global itemNum
    c.acquire()     # 锁住资源
    while 0 == itemNum:     # 如无产品则让线程等待
        print("consumer :挂起.", threading.current_thread().name, threading.current_thread())
        c.wait()
    itemNum -= 1
    print("consumer : 消费 %s." % item, itemNum, threading.current_thread().name, threading.current_thread())
    c.release()     # 解锁资源

# 生产者
def producer():
    global item     # 商品编号
    global itemNum
    time.sleep(3)
    c.acquire()     # 锁住资源
    item = random.randint(1, 1000)
    itemNum += 1
    print("producer : 生产 %s." % item, threading.current_thread().name, threading.current_thread())
    c.notifyAll()   # 唤醒所有等待的线程--》其实就是唤醒消费者进程
    c.release()     # 解锁资源


threads = []  # 线程收集列表

for i in range(0, 4):  # 使用循环完成生产者与消费者线程的建立
    t1 = Thread(target=producer, name=f'pro_{i}')
    t2 = Thread(target=consumer, name=f"cos_{i}")
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:  # 等待所有线程完成
    t.join()
