'''
零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:你可以认为每种硬币的数量是无限的。
'''

'''
dp[j]表示金额为j时所需最少硬币数
dp[j] = min(dp[j], dp[j-coins[i]]+1)
时间复杂度：O(NW)，空间复杂度：O(W)。N：硬币种数，W：目标金额
'''
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]


if __name__ == '__main__':
    s = Solution()
    coins = [2] #[1, 2, 5]
    amount = 3  #11
    print(s.coinChange(coins, amount))
