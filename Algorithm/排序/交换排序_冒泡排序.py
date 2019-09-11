import random

'''
冒泡排序
    时间复杂度：O(n)~O(n^2)
    空间复杂度：O(1)
    稳定性：稳定
'''
def bubbleSort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(n):  # 最多做n-1趟冒泡
        flag = 0
        for j in range(n-1, i, -1):     # 对当前无序区自下向上扫描
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                flag = 1
        if flag == 0:                   # 本趟排序未发生交换，提前终止算法
            break
    return array

if __name__ == '__main__':
    array = random.sample(range(2000), 20)
    print(bubbleSort(array))