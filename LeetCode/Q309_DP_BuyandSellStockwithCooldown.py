# 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#     你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#     卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
# 示例:
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0

        cool = 0            # cool表示第i天为冷冻状态的最大收益
        buy  = -prices[0]   # buy表示第i天为可买入状态的最大收益；第一天一定是买入，初始化为第一个股票价格的负值
        sell = 0            # sell表示第i天为可卖出状态的最大收益

        for i in range(1, n):
            cool_pre = cool
            buy_pre = buy
            sell_pre = sell
            cool = sell_pre                             # 冷冻状态的最大收益 =  从可卖出状态转移过来
            buy = max(buy_pre, cool_pre - prices[i])    # 可买入状态的最大收益 =  max(保持可买入状态，从冷冻状态转移过来)
            sell = max(sell_pre, buy_pre + prices[i])   # 可卖出状态的最大收益 =  max(保持可卖出状态，从可买入状态转移过来)

        return sell         #最后一定是卖出

if __name__ == '__main__':
    s = Solution()
    prices = [1,2,3,0,2]
    print(s.maxProfit(prices))