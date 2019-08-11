# 小明有10000台设备，想以每台均价D（浮点数，尽可能接近）元卖出去，只收整数数额的钱。
# 卖出去台数N，共售价M。
# 输入浮点数D（0<D<10）；输出M、N，若多种方案均价一样，输出台数小的。
# 示例1：
# 输入：3.14159265358979
# 输出：355 113


import math

if __name__ == '__main__':
    d = float(input())
    err = float('inf')

    res_m, res_n = 0, 0
    for n in range(1, 10001):
        m = math.ceil(n * d)
        tmp = abs(m/n-d)
        if err > tmp:
            err = tmp
            res_m = m
            res_n = n

    print(str(res_m) + ' ' + str(res_n))