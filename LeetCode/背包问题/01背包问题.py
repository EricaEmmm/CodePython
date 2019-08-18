'''
有N件物品和一个容量是W的背包。每件物品只能使用一次。第i件物品的重量是wi，价值是vi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
输入格式
第一行两个整数，N，W，用空格隔开，分别表示物品数量和背包容积。
接下来有N行，每行两个整数wi,vi，用空格隔开，分别表示第i件物品的重量和价值。
输出格式
输出一个整数，表示最大价值。
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
'''

'''
dp[i][j]表示前i个物品放入容量为j的背包可获得最大的价值
时间复杂度：O(NW)，空间复杂度：O(NW)
'''
def ZeroOnePack(N, W, v, w):
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[N][W]

'''
dp[j]表示容量为j的背包可获得最大的价值
时间复杂度：O(NW)，空间复杂度：O(W)
'''
def ZeroOnePack1(N, W, v, w):
    dp = [0 for _ in range(W+1)]
    for i in range(1, N+1):
        for j in range(W, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])
    return dp[W]


if __name__ == '__main__':
    N, W = list(map(int, input().split()))
    w, v = [0 for _ in range(N+1)], [0 for _ in range(N+1)]
    for i in range(1, N+1):
        w[i], v[i] = list(map(int, input().split()))

    print(ZeroOnePack1(N, W, v, w))
