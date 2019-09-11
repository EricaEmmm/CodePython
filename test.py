import math
def c(m, n):
    return math.factorial(n) / (math.factorial(m)*math.factorial(n-m))


if __name__ == '__main__':
    res = 0
    for i in range(199):
        res += c(i, 250+2*i)
    res2 = 0
    for i in range(249):
        res2 += c(i, 200+2*i)

    print(res/(res+res2))
