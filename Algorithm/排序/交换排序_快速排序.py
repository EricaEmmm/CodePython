import random

'''
快速排序
    时间复杂度：O(nlogn)~O(n^2)
    空间复杂度：O(nlogn)~O(n)
    稳定性：不稳定
'''
def Partition(array, left, right):
    pivot = array[left]
    while left < right:
        while left < right and array[right] >= pivot:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= pivot:
            left += 1
        array[right] = array[left]
    array[left] = pivot
    return left

# 递归
def quickSort(array, left, right):
    if left < right:
        pivot = Partition(array, left, right)
        quickSort(array, left, pivot-1)
        quickSort(array, pivot+1, right)
    return array


# 非递归
def quickSort2(array):
    n = len(array)
    if n < 2:
        return array
    sta = [(0, n-1)]
    while sta:
        left, right = sta.pop()
        if left < right:
            pivot = Partition(array, left, right)
            sta.append((left, pivot-1))
            sta.append((pivot+1, right))
    return array


if __name__ == '__main__':
    array = random.sample(range(2000), 20)
    # print(quickSort(array, 0, len(array)-1))
    print(quickSort2(array))