
def pow(n, k):
    res = 1
    while k:
        if k&1:
            res = res*n%1000000007
            n = n*n%1000000007
            k = k>>1
    return res

def cal(n, k):
    res = pow(k-1, n)
    if res & n & 1:
        res = 1000000007 - res
    res += k-1
    if res >= 1000000007:
        res -= 1000000007
    res = res * pow(k, 1000000005)%1000000007
    if res & n & 1:
        res = 1000000007 - res
    return res


def main():
    # k, n = list(map(int, input().split()))
    print(cal(3, 3))

main()