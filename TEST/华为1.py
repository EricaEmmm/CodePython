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