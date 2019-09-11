'''
有N组物品和一个容量是V的背包。每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是vij，价值是wij，其中i是组号，j是组内编号。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。输出最大价值。
输入格式
第一行有两个整数N，V，用空格隔开，分别表示物品组数和背包容量。
接下来有N组数据：
    每组数据第一行有一个整数Si，表示第i个物品组的物品数量；
    每组数据接下来有Si行，每行有两个整数vij,wij，用空格隔开，分别表示第i个物品组的第j个物品的体积和价值；
输出格式
输出一个整数，表示最大价值。
输入样例
3 5
2
1 2
2 4
1
3 4
1
4 5
输出样例：
8
'''

'''
dp[j]表示容量为j的背包可获得最大的价值
'''
def GroupPack(N, V, v, w):
    dp = [0 for _ in range(V+1)]
    for i in range(N):  # 枚举组数
        for j in range(V, -1, -1):  # 枚举背包空间
            for k in range(len(v[i])):  # 枚举每组物品
                if j >= v[i][k]:
                    dp[j] = max(dp[j], dp[j-v[i][k]]+w[i][k])
    return dp[V]

if __name__ == '__main__':
    N, V = list(map(int, input().split()))
    v, w = [[] for _ in range(N)], [[] for _ in range(N)]
    for i in range(N):
        s = int(input())
        for j in range(s):
            a, b = list(map(int, input().split()))
            v[i].append(a)
            w[i].append(b)
    print(GroupPack(N, V, v, w))