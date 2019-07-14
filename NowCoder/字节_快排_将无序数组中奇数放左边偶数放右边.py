

def odd_even(List):
    """
    思想类似快排，原地置换
    时间复杂度：O(n)，空间复杂度：O(1)
    """
    left, right = 0, len(List)-1
    while left < right:
        while left < right and List[left] / 2 != 0:
            left += 1
        while left < right and List[right] / 2 == 0:
            right -= 1
        List[left], List[right] = List[right], List[left]
    return List


if __name__ == '__main__':
    List = [2,6,4,1,3,5]
    print(odd_even(List))