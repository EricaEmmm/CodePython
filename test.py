
from queue import Queue
from tool import SmallHeap, BigHeap, heapq
from collections import Counter

if __name__ == '__main__':
    s = "1223"
    tel = [int(i) for i in s]
    count_dct = Counter(tel)
    idx = list(range(len(tel)))
    print(count_dct)

    t = [1,2,3,4]
    t.pop()
    print(t)
