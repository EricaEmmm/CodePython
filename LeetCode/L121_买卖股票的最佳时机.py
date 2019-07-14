# 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution(object):
    # 暴力法——超时
    # 时间复杂度：O(n^2)，空间复杂度：O(1)
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > res:
                    res = profit
        return res

    # 动态规划
    # 最大利润 = max{前一天最大利润, 今天的价格 - 之前最低价格}
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")  # 不能用prices[0]，有可能数组为空，要用正无穷
        maxProfit = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            elif i - minPrice > maxProfit:
                maxProfit = i - minPrice
        return maxProfit

    def maxProfit(self, prices):
        return self.maxProfit2(prices)

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4] # [7,6,4,3,1] #
    print(s.maxProfit(prices))
