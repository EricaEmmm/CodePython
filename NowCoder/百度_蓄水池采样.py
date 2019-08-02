# 给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，
# 请问如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出k个不重复的数据。

import random
from collections import Counter

class ReservoirSample():
    def __init__(self, k):
        self.k = k
        self.n = 0
        self._sample = []

    def feed(self, item):
        self.n += 1
        # 第i个元素（i <= k），直接进入池中
        # 最后被选中的概率 = 第一次被选中的概率 * 之后不被替换的概率
        #                  = 第一次被选中的概率 * 第一次不被替换的概率 * 第二次不被替换的概率 * ... * 第n次不被替换的概率
        #                  =          1         *       k/(k+1)        *       (k+1)/(k+2)    * ... *       (n-1)/n
        #                  =  k/n
        if self.n <= self.k:
            self._sample.append(item)
            return self._sample
        # 第i个元素（i > k），以k/i的概率进入池中
        # 最后被选中的概率 = 被选中的概率 * 之后不被替换的概率
        #                  = 被选中的概率 * 第一次不被替换的概率 * 第二次不被替换的概率 * ... * 第n次不被替换的概率
        #                  =      k/i     *       i/(i+1)        *       (i+1)/(i+2)    * ... *       (n-1)/n
        #                  =  k/n
        else:
            rand_int = random.randint(1, self.n)
            if  rand_int <= self.k:
                self._sample[rand_int-1] = item
            return self._sample


if __name__ == '__main__':
    samples = []
    for i in range(100000):
        sample = []
        rs = ReservoirSample(4)
        for item in range(1, 11):
            sample = rs.feed(item)
        samples.extend(sample)

    res = Counter(samples)
    print(res)


