from collections import Counter

def solve(n, list_in):
    """定义一个1*N的数组，每一列落下方块时，对应数组位置+1，满了就减1"""
    # res = 0
    # m = len(list_in)
    # col = [0 for i in range(n)]
    # for i in range(m):
    #     col[list_in[i]-1] += 1
    #     for j in range(n):
    #         if col[j] == 0:
    #             if j == n-1:
    #                 j -= 1
    #             break
    #     if j == n-1:
    #         res += 1
    #         for i in range(n):
    #             col[i] -= 1
    # return res
    """定义一个1*N的数组，每一列落下方块时，对应数组位置+1，取数组的最小值"""
    m = len(list_in)
    col = [0 for i in range(n)]
    for i in range(m):
        col[list_in[i]-1] += 1
    return min(col)



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    array = list(map(int, input().split()))

    dic = Counter(array)
    if len(dic) < n:
        print(0)
    else:
        print(min(dic.values()))