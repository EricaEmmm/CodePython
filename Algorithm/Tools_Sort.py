import time
import random
import sys

sys.setrecursionlimit(100000)   # 解决超过最大递归深度问题：maximum recursion depth exceeded in comparison


# ------------------------------
# 冒泡排序
# ------------------------------
def bubbleSort1(List):
    """
    交换排序之冒泡排序：从头至尾冒泡
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    n = len(List)
    for i in range(n):
        for j in range(i, n):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    return List

def bubbleSort2(List):
    """
    交换排序之冒泡排序：从尾至头冒泡
    时间复杂度：O(n)-O(n^2)
    空间复杂度：O(1)
    """
    n = len(List)
    for i in range(n):  # 最多做n-1趟冒泡
        exchange_flag = False
        for j in range(n-1, i-1, -1):   # 对当前无序区自下向上扫描
            if List[j] < List[j-1]:
                List[j], List[j-1] = List[j-1], List[j]
                exchange_flag = True
        if exchange_flag == False:      # 本趟排序未发生交换，提前终止算法
            return List
    return List


# ------------------------------
# 快速排序
# ------------------------------
def Partition(List, low, high):
    """
    划分函数：找到一个分组标准，让它左边的值比它小，右边的值比它大
    :param List:  待排序序列
    :param low:   序列最小下标值
    :param high:  序列最大下标值
    :return:      分组基准
    """
    pivot = List[low]
    while low < high:
        # 从右向左扫描找到第一个小于pivot的值，将其与下标low的值交换
        while low < high and List[high] >= pivot:   # 注意 = ！！！
            high -= 1
        List[low] = List[high]
        # 从左向右扫描找到第一个小于pivot的值，将其与下标high的值交换
        while low < high and List[low] <= pivot:
            low += 1
        List[high] = List[low]
    List[low] = pivot
    return low

def q_sort(List, low, high):
    """
    :param List:  待排序序列
    :param low:   序列最小下标值
    :param high:  序列最大下标值
    :return:      排序序列
    """
    if low < high:
        pivot = Partition(List, low, high)  # 划分后的基准位置
        q_sort(List, low, pivot-1)          # 对左区间递归排序
        q_sort(List, pivot+1, high)         # 对右区间递归排序
    return List

def quickSort(List):
    """
    交换排序之快速排序
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """
    # return q_sort(List, 0, len(List)-1)

    q_sort(List, 0, len(List) - 1)
    return List


# ------------------------------
# 归并排序
# ------------------------------
def merge_two(List1, List2):
    """
    对两个已排序的数组进行排序合并
    :param List1:  已排序的数组1
    :param List2:  已排序的数组2
    :return:       合并后的数组
    """
    res = []
    i, j = 0, 0
    while i < len(List1) and j < len(List2):
        if List1[i] < List2[j]:
            res.append(List1[i])
            i += 1
        else:
            res.append(List2[j])
            j += 1

    # 将List1或List2剩余元素加到合并数组
    for k in range(i, len(List1)):
        res.append(List1[k])
    for k in range(j, len(List2)):
        res.append(List2[k])
    return res

def mergeSort(List):
    """
    归并排序
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    :param List: 待排序的数组
    :return:     排序后的数组
    """
    if len(List) < 2:
        return List
    mid = len(List) // 2

    # 对原问题进行分解
    List1 = List[:mid]
    List2 = List[mid:]

    # 对分解后的子问题进行求解
    mergeSort(List1)
    mergeSort(List2)

    # 将子问题合并
    return merge_two(List1, List2)


# ------------------------------
# 桶排序
# ------------------------------
def bucketSort(List):
    """
    桶排序
    时间复杂度：O(n)+O(m*(n/m)*log(n/m))=O(n+nlogn-nlogk))，当k接近n时，近似为O(n)
    空间复杂度：O(n+k)
    :param List: 待排序的数组
    :return:     排序后的数组
    """
    # 确定元素的最值
    dmin = min(List)
    dmax = max(List)

    # 桶数：(dmax - dmin) / length的结果为数组大小的倍数（最大倍数）
    bucketNum = (dmax - dmin) // len(List) + 1

    # 初始化桶，将每个元素放入桶
    bucket = [[] for i in range(bucketNum)]
    for i in List:
        num = (i - dmin) // len(List)
        bucket[num].append(i)

    # 用快速排序对每个桶进行排序
    for i in bucket:
        quickSort(i)

    res = []
    # 合并数据
    for i in bucket:
        for j in i:
            res.append(j)

    return res



if __name__ == '__main__':
    List = [49, 38, 65, 97, 76, 13, 27, 49]#random.sample(range(10000),2000)# [i for i in range(5000)] #
    #
    # # 冒泡排序
    # # start = time.time()
    # # print(bubbleSort1(List))
    # # print(f'set time:{time.time()-start}')
    # start = time.time()
    # print(bubbleSort2(List))
    # print(f'冒泡排序 set time:{time.time()-start}')

    # 快速排序
    # Partition(List, 0, 7)     # List会被改变
    # Partition(List[:], 0, 7)
    # print(List)
    start = time.time()
    print(quickSort(List))
    print(f'快速排序 set time:{time.time() - start}')

    # # 归并排序
    # start = time.time()
    # print(mergeSort(List))
    # print(f'归并排序 set time:{time.time() - start}')
    #
    # # 桶排序
    # start = time.time()
    # print(bucketSort(List))
    # print(f'桶排序 set time:{time.time() - start}')

