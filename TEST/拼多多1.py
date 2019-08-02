



if __name__ == '__main__':
    a = [19,20,20]  #list(map(int, input().split()))   # [20,1,23]   # [1,3,7,4,10]
    b = [21]  #list(map(int, input().split()))   # [50,26,7]   # [2,1,5,8,9]

    n = len(a)
    pre = a[0]
    for i in range(1, n):
        if a[i] <= pre:
            break
        else:
            pre = a[i]

    flag = 0
    b.sort(reverse=True)
    if i+1 == n:
        for j in b:
            if j > a[i-1]:
                a[i] = j
                flag = 1
                break
    elif i-1 == 0:
        for j in b:
            if j < a[i+1] and j > a[i-1]:
                a[i] = j
                flag = 1
                break
    elif i-1 > 0:
        for j in b:
            if j < a[i+1] and j > a[i-1]:
                a[i] = j
                flag = 1
                break
            if j < a[i] and j > a[i-2]:
                a[i-1] = j
                flag = 1
                break

    if flag == 1:
        print(' '.join(map(str, a)))
    else:
        print('NO')