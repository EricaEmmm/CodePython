

if __name__ == '__main__':
    """输入"""
    # 矩阵维度
    n, m = map(int, input().split())    # 通过指定分隔符对字符串进行切片，输出是字符串列表，需转化为int
    print(n,m)
    # 数组
    list_in = []
    list_in = list(map(int, input().split()))
    print(list_in)
    # 矩阵
    matrix_in = []
    for i in range(m):  # m行
        matrix_in.append(list(map(int, input().split())))
    print(matrix_in)
