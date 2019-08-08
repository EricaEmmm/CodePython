# 凑零钱找组合
# 输入：
# 6 5 4 3 2 1
# 11
# 输出：
# 12


def process(ChargeNum, targetNum):
    ChargeSet = [1, 5, 10, 20, 50, 100]
    ChargeList = {}
    for i in range(len(ChargeNum)):
        ChargeList[ChargeSet[i]] = ChargeNum[i]
    for


if __name__ == '__main__':
    # ChargeNum = list(map(int, input().split()))
    # targetNum = int(input())
    ChargeSet = [1, 5, 10, 20, 50, 100]
    print(ChargeSet)

