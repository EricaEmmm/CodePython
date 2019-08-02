if __name__ == '__main__':
    n = 10   #int(input())
    l = [1,2,3,4,5,6,7,8,9,10] #list(map(int, input().split()))
    w = [1,1,1,1,1,1,1,1,1,10] #list(map(int, input().split()))
    lw = [i for i in zip(*[l, w])]
    lw.sort(key = lambda x: x[0], reverse = True)

    sum = 0
    res = []
    for i in range(n):
        res.append(lw[i])
        flag = 1
        for j in range(0, len(res)):
            if len(res) == 1:
                continue
            if 7*res[j][1] < sum(res[j+1:][1]):
                flag = 0
        if flag == 1:
            sum += 1
        else:
            res.pop()

    print(sum)