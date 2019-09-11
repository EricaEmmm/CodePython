'''
有N件物品和一个容量是V的背包，背包能承受的最大重量是M。每件物品只能用一次。体积是vi，重量是mi，价值是wi。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。
输入格式
第一行两个整数，N，V，M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。
接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。
输出格式
输出一个整数，表示最大价值。
输入样例
4 5 6
1 2 3
2 4 4
3 4 5
4 5 6
输出样例：
8
'''

'''
dp[j][k]表示背包剩余体积是j，剩余重量是k时可获得最大的价值
'''
def Cost2DPack(N, V, M, v, m, w):
    dp = [[0 for i in range(V+1)] for j in range(M+1)]
    for i in range(1, N+1): # 枚举物品数量
        for j in range(V, v[i]-1, -1):  # 枚举背包剩余体积
            for k in range(M, m[i]-1, -1):  # 枚举背包剩余重量
                dp[k][j] = max(dp[k][j], dp[k-m[i]][j-v[i]]+w[i])
    return dp[M][V]

if __name__ == '__main__':
    N, V, M = list(map(int, input().split()))
    v, m, w = [0 for i in range(N+1)], [0 for i in range(N+1)], [0 for i in range(N+1)]
    for i in range(1, N+1):
        v[i], m[i], w[i] = list(map(int, input().split()))
    print(Cost2DPack(N, V, M, v, m, w))