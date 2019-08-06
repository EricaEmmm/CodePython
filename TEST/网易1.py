def main():
    n = int(input())
    array = list(map(int, input().split()))
    res = []
    for i in range(n):
        res.append(n+1-array[i])
    print(' '.join(map(str, res)))

main()