# 凑零钱找组合
# 输入：
# 6 5 4 3 2 1
# 11
# 输出：
# 12


def process(ChargeNum, targetNum):
    # ChargeSet = [1, 5, 10, 20, 50, 100]
    # ChargeList = {}
    # for i in range(len(ChargeNum)):
    #     ChargeList[ChargeSet[i]] = ChargeNum[i]
    res = 0
    for i in range(ChargeNum[0]+1):
        for j in range(ChargeNum[1]+1):
            for k in range(ChargeNum[2]+1):
                for m in range(ChargeNum[3]+1):
                    for n in range(ChargeNum[4]+1):
                        for l in range(ChargeNum[5]+1):
                            if i+j*5+k*10+m*20+n*50+l*100 == targetNum:
                                res += i+j+k+m+n+l
    return res if res else -1



if __name__ == '__main__':
    ChargeNum = list(map(int, input().split()))
    targetNum = int(input())
    print(process(ChargeNum, targetNum))

