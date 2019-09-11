import random

'''
桶排序
    时间复杂度：O(n+nlogn-nlogk)
    空间复杂度：O(n)
    稳定性：稳定
'''
def bucketSort(array):
    n = len(array)
    if n <= 1:
        return array

    # 桶数：(dmax - dmin) / length的结果为数组大小的倍数（最大倍数）
    # O(n)
    nums = (max(array)-min(array)) // n + 1

    # 初始化桶，将每个元素放入桶
    # O(n)
    bucket = [[] for i in range(nums)]
    for i in range(n):
        bucket[(array[i]-min(array))//n].append(array[i])

    # 对每个桶进行排序，合并数据
    # O(k)O(n/klogn/k)
    res = []
    for num in range(nums):
        bucket[num].sort()
        res.extend(bucket[num])

    return res

if __name__ == '__main__':
    array = random.sample(range(200), 20)
    print(bucketSort(array))