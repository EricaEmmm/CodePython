
def sequentialSearch(x, array):
    """
    顺序查找
    时间复杂度：O(n)
    """
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1

def binarySearch(x, array):
    """
    二分查找
    时间复杂度：O(logn)
    """
    for i in range(len(array)):
        if array[i] == x:
            return i


if __name__ == '__main__':
    a = [1, 3, 5, 2, 0, 9, 8, 4, 7, 6]
    x = 2
    print(sequentialSearch(x, a))