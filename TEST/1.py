
def main():
    k, n = list(map(int, input().split()))
    tmp1, tmp2 = 1, 1
    for i in range(k):
        tmp1 = tmp1 * (n-1)% 1000000007
        tmp2 = tmp2 * (-1)
    print(int((tmp1 + (n-1)*tmp2)/n ))

main()