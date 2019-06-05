# 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m, n = len(obstacleGrid[0]), len(obstacleGrid)
        # dp = [[1 for i in range(m)] for j in range(n)]
        # # 起始点不能为障碍
        # if obstacleGrid[0][0] == 0:
        #     dp[0][0] = 1
        # else:
        #     return 0
        # # 结束点不能为障碍
        # if obstacleGrid[n-1][m-1] == 1:
        #     return 0
        # # 初始化两条边
        # if n > 2:
        #     for i in range(1, n):
        #         if obstacleGrid[i][0] == 0:
        #             dp[i][0] = dp[i-1][0]
        #         else:
        #             dp[i][0] = 0
        # if m > 2:
        #     for i in range(1, m):
        #         if obstacleGrid[0][i] == 0:
        #             dp[0][i] = dp[0][i-1]
        #         else:
        #             dp[0][i] = 0
        # # 动态规划，从上边或左边来的路径是障碍，就将它们置0
        # for i in range(1, n):
        #     for j in range(1, m):
        #         if obstacleGrid[i-1][j] == 1:
        #             dp[i-1][j] = 0
        #         if obstacleGrid[i][j-1] == 1:
        #             dp[i][j-1] = 0
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[n-1][m-1]

        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(0, n):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for i in range(0, m):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1
        # 动态规划，从上边或左边来的路径是障碍，就将它们置0
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]
        # [0,0,0],
        # [0,1,0],
        # [0,0,0]
    ]
    print(s.uniquePathsWithObstacles(obstacleGrid))