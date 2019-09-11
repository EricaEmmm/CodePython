'''
有N种物品和一个容量是W的背包。
物品一共有三类：
    第一类物品只能用1次（01背包）；
    第二类物品可以用无限次（完全背包）；
    第三类物品最多只能用 si 次（多重背包）；
    每种重量是wi，价值是vi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。输出最大价值。
输入格式
第一行两个整数，N，W，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的重量、价值和数量。
    si=−1   表示第 i 种物品只能用1次；
    si=0    表示第 i 种物品可以用无限次；
    si>0    表示第 i 种物品可以使用 si 次；
输出格式
输出一个整数，表示最大价值
输入样例
4 5
1 2 -1
2 4 1
3 4 0
4 5 2
输出样例：
8
'''

# 时间复杂度：O(W)
def ZeroOnePack(W, v, w, dp):
    for j in range(W, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)

# 时间复杂度：O(W)
def CompletePack(W, v, w, dp):
    for j in range(w, W+1):
        dp[j] = max(dp[j], dp[j-w]+v)

# 时间复杂度：O(W∑logsi)
def MultiplePack(W, v, w, s, dp):
    if s * w > W:
        CompletePack(W, v, w, dp)
    else:
        k = 1
        while k < s:
            ZeroOnePack(W, v*k, w*k, dp)
            s -= k
            k *= 2
        ZeroOnePack(W, v * s, w * s, dp)

'''
dp[j]表示容量为j的背包可获得最大的价值
'''
def MixPack(N, W, v, w, s):
    dp = [0 for _ in range(W+1)]
    for i in range(1, N+1):
        if s[i] == -1:
            ZeroOnePack(W, v[i], w[i], dp)
        elif s[i] == 0:
            CompletePack(W, v[i], w[i], dp)
        else:
            MultiplePack(W, v[i], w[i], s[i], dp)
    return dp[W]

if __name__ == '__main__':
    N, W = list(map(int, input().split()))
    w, v, s = [0 for _ in range(N+1)], [0 for _ in range(N+1)], [0 for _ in range(N+1)]
    for i in range(1, N+1):
        w[i], v[i], s[i] = list(map(int, input().split()))

    print(MixPack(N, W, v, w, s))