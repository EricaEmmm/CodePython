import random

'''
归并排序——递归
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    稳定性：稳定
'''
def mergeTwo(array1, array2):
    i, j = 0, 0
    res = []
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:  # 《= 保证处在前面序列的相等的元素，保存在结果序列的前面
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    # 将List1或List2剩余元素加到合并数组
    res.extend(array1[i:])
    res.extend(array2[j:])
    return res

def mergeSort(array):
    if len(array) <= 1:
        return array

    # 递归地分解数列
    mid = len(array) // 2
    array1 = mergeSort(array[:mid])
    array2 = mergeSort(array[mid:])

    # 递归地合并数列
    return mergeTwo(array1, array2)

'''
归并排序——非递归
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    稳定性：稳定
'''
def merge(array, left, mid, right):
    i, j = left, mid
    res = []
    while i < mid and j < right:
        if array[i] <= array[j]:
            res.append(array[i])
            i += 1
        else:
            res.append(array[j])
            j += 1
    res.extend(array[i:mid])
    res.extend(array[j:right])
    array[left:right] = res

def mergePass(array, k):
    i = 0
    while i + 2 * k <= len(array):
        merge(array, i, i+k, i+2*k)
        i += 2 * k
    if i + k < len(array):
        merge(array, i, i+k, len(array))

def mergeSortNonRe(array):
    if len(array) < 2:
        return array
    k = 1
    while k <= len(array):
        mergePass(array, k)
        k *= 2
    return array


if __name__ == '__main__':
    array = random.sample(range(200), 20)
    print(mergeSort(array))
    print(mergeSortNonRe(array))