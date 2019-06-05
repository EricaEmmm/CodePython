# 不同路径
# 一个机器人位于一个 m x n（列 x 行） 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#
# 示例 2:
# 输入: m = 7, n = 3
# 输出: 28

"""
排列问题：从n个不同元素中，任取m(m≤n）个元素按照一定的顺序排成一列,所有排列的个数
A(m,n) = n(n-1)(n-2)……(n-m+1)
       = n! / (n-m)!

组合问题：从n个不同元素中，任取m(m≤n）个元素并成一组,所有组合的个数
C(m,n) = n(n-1)(n-2)……(n-m+1) / m!
       = A(m,n) / m!
       = n! / m!(n-m)!
"""
import math
from functools import reduce

class Solution(object):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    def uniquePaths1(self, m, n):
        """
        机器人一共要走 m+n-2 步，且一定是向右 m-1 步，向左 n-1 步，
        即转化为组合问题C(m-1, m+n-2)或C(n-1, m+n-2)
        """
        # 法一：
        # return math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))  # C(m-1, m+n-2)
        # 法二：
        tmp = min(m, n)
        dividend, divisor = 1, 1
        for i in range(1,tmp):
            dividend *= m+n-1-i
            divisor *= i
        return dividend/divisor

    def uniquePaths2(self, m, n):
        """
        暴力法：超时
        """
        return self.getPath(m, n)
    def getPath(self, m, n):
        if m == 1 | n == 1:     #只要到最下边或最右边，就只能沿着边走到终点了
            return 1
        return self.getPath(m-1, n) + self.getPath(m, n-1)

    def uniquePaths3(self, m, n):
        """
        动态规划：dp[i][j]=dp[i - 1][j] + dp[i][j - 1]，表示到当前位置的不同走法的个数
        """
        dp = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n-1][m-1]

    def uniquePaths(self, m, n):
        return self.uniquePaths3(m, n)

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(2, 1))
    # dp = [[0 for i in range(3)] for j in range(3)]
    # print(dp)