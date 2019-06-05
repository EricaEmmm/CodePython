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
    # """输入"""
    # # 矩阵维度
    # n, m = map(int, input().split())    # 通过指定分隔符对字符串进行切片，输出是字符串列表，需转化为int
    # # print(n,m)
    # # 数组
    # list_in = []
    # list_in = list(map(int, input().split()))
    # # print(list_in)
    #
    # """解决"""
    # res = solve(n, list_in)
    #
    # """输出"""
    # print(res)
    #
    # # t = [[] for i in range(3)]
    # # t[1] = [1,2,3]
    # # t[1] = t[1][1:]
    # # print(t)
    # list1 = "abcde"#[1, 2, 3, 4, 5, 6]
    # list1 = list1[3:1:-1]
    # print(list1)
    #
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # new = [reversed(i) for i in matrix]
    # print([i for i in zip(*matrix)])
    #
    # matrix.sort(key = lambda x : x.start)
    # print(matrix)

    n = [1,2,3]
    print(n[-1])