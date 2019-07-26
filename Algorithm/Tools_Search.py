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
    low, high = 0, len(array)
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    a = [1,4,7,8,9,12,45,77] #[1, 3, 5, 2, 0, 9, 8, 4, 7, 6]
    x = 8
    print(binarySearch(x, a))