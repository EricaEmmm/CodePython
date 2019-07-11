# 输入n，求一个nXn矩阵，规定矩阵沿45度递增，形成一个zigzag数组(JPEG编码里取像素数据的排列顺序)，
# 请问如何用实现？
# n = 8
# 0     1     5     6     14    15    27    28
# 2     4     7     13    16    26    29    42
# 3     8     12    17    25    30    41    43
# 9     11    18    24    31    40    44    53
# 10    19    23    32    39    45    52    54
# 20    22    33    38    46    51    55    60
# 21    34    37    47    50    56    59    61
# 35    36    48    49    57    58    62    63

def Zigzag(n):
    # 分配空间
    res = [ [0 for i in range(n)] for j in range(n)]

    # 数组赋值
    for i in range(n):
        for j in range(n):
            if i + j < n:
            # 左上三角矩阵
            # 设二维数组的某个下标为（i, j），那么下标和s = i + j
            # 第s条斜线的数字个数为s + 1个，前s条斜线共有1 + 2 + ... + s = s(s+1)/2个数字
            # 某斜线上的数字a[i][j]：下标和为奇数时，表示为s(s + 1) / 2 + i；
            #                        下标和为偶数时，表示为s(s + 1) / 2 + j
                s = i + j
                res[i][j] = s * (s + 1) // 2 + (j if ((i+j)%2 == 0) else i)
            else:
            # 右下三角矩阵
            # 右下数起，相对于n*n所减去的值不断加1
            # 右下数起，第s条（s大于等于0）斜线与下标i和j的关系：s = (n - 1 - i) + (n - 1 - j)
            # 第s条斜线及其右方共有D = 1 + 2 + ... + s = s(s+1)/2个数字
            # 第s条斜线上的第k个元素减去的值为D + k，下标和为奇数时，k = n - i
            #                                        下标和为偶数时，k = n - j
                s = (n - 1 - i) + (n - 1 - j)
                res[i][j] = n*n - ( s*(s+1)//2 + n-(j if ((i + j) % 2 == 0) else i))
    return res


if __name__ == '__main__':
    print(Zigzag(7))