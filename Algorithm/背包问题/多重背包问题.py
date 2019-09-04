'''
有N种物品和一个容量是W的背包。第i种物品最多有si件，每件重量是wi，价值是vi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
输入格式
第一行两个整数，N，W，用空格隔开，分别表示物品种数和背包容积。
接下来有N行，每行三个整数wi，vi，si，用空格隔开，分别表示第i种物品的重量、价值、数量。
输出格式
输出一个整数，表示最大价值。
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
'''


'''
dp[i][j]表示前i种物品放入容量为j的背包可获得最大的价值
时间复杂度：O(NW∑si)，空间复杂度：O(NW)
'''
def MultiplePack1(N, W, v, w, s):
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1): # 枚举物品种类
        for j in range(1, W+1): # 枚举背包空间
            for k in range(s[i]+1):
                if j >= k*w[i]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-k*w[i]]+k*v[i])
    return dp[N][W]

'''
二进制优化
dp[j]表示容量为j的背包可获得最大的价值
时间复杂度：O(NW∑logsi)，空间复杂度：O(W)
'''
def ZeroOnePack(dp, W, v, w):
    for j in range(W, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)

def CompletePack(dp, W, v, w):
    for j in range(w, W+1):
        dp[j] = max(dp[j], dp[j-w]+v)

def MultiplePack2(N, W, v, w, s):
    dp = [0 for _ in range(W+1)]
    for i in range(1, N+1):  # 枚举物品种类
        if s[i]*w[i] >= W:      # 若总容量比某种物品的容量要小，则对该物品用完全背包
            CompletePack(dp, W, v[i], w[i])
        else:                   # 否则就将多重背包转化为01背包
            k = 1
            while k < s[i]:
                ZeroOnePack(dp, W, k*v[i], k*w[i])
                s[i] -= k
                k *= 2
            ZeroOnePack(dp, W, s[i]*v[i], s[i]*w[i])
    return dp[W]


if __name__ == '__main__':
    N, W = list(map(int, input().split()))
    w, v, s = [0 for _ in range(N+1)], [0 for _ in range(N+1)], [0 for _ in range(N+1)]
    for i in range(1, N+1):
        w[i], v[i], s[i] = list(map(int, input().split()))

    print(MultiplePack2(N, W, v, w, s))
