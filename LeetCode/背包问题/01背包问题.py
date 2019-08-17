'''
有N件物品和一个容量是V的背包。每件物品只能使用一次。第i件物品的体积是vi，价值是wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有N行，每行两个整数vi,wi，用空格隔开，分别表示第i件物品的体积和价值。
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
'''
def ZeroOnePack(N, V, v, w):
    dp = [[0 for i in range(N)] for j in range(V+1)]
    for i in range(1, N):
        for j in range(V+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N-1][V]

if __name__ == '__main__':
    N, V = 4, 5  # list(map(int, input().split()))
    v, w = [1,2,3,4], [2,4,4,5]# [], []
    # for i in range(N):
    #     v[i], w[i] = list(map(int, input().split()))

    print(ZeroOnePack(N, V, v, w))
