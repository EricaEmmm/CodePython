import random

'''
直接选择排序
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    稳定性：不稳定
'''
def selectSort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(n):
        # 选定首位为最小值
        minIdx = i
        # 找到最小值下标
        for j in range(i+1, n):
            if array[j] < array[minIdx]:
                minIdx = j
        # 交换
        if minIdx > i:
            array[minIdx], array[i] = array[i] , array[minIdx]
    return array

    return array

if __name__ == '__main__':
    array = random.sample(range(2000), 20)
    print(selectSort(array))