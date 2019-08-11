def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        array.sort()
        res = [0 for _ in range(n)]
        if n%2:    # 奇数
            for j in range(n//2):
                res[j*2+1] = array[n//2+j]
                res[j*2] = array[j]
            res[-1] = array[n//2]
        else:
            for j in range(n//2):
                res[j*2+1] = array[n//2+j]
                res[j*2] = array[j]
        flag = 1
        for i in range(n):
            if i+1 == n:
                if array[i] > array[i - 1] + array[-1]:
                    flag = 0
            else:
                if array[i] > array[i-1]+array[i+1]:
                    flag = 0
        if flag == 0:
            print('NO')
        else:
            print('YES')

main()