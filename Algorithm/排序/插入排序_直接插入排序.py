import random

'''
直接插入排序
    时间复杂度：O(n)~O(n^2)
    空间复杂度：O(1)
    稳定性：稳定
'''
def insertSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        tmp = array[i]
        for j in range(i-1, -1, -1):
            if tmp < array[j]:
                array[j+1] = array[j]
            else:
                array[j+1] = tmp
                break
    return array

if __name__ == '__main__':
    array = random.sample(range(2000), 20)
    print(insertSort(array))