# 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution(object):
    # 法一：超时
    # 从第一层向下走，路径和的最小值（有多少条路径，就有多少个路径和）
    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = []
        self.countPath(triangle, 0, 0, 0, res)
        return min(res)

    def countPath(self, triangle, level, location, total, res):
        if level == len(triangle):
            res.append(total)
            return
        total += triangle[level][location]
        self.countPath(triangle, level+1, location, total, res)
        total -= triangle[level][location]
        if location+1 < len(triangle[level]):
            total += triangle[level][location+1]
            self.countPath(triangle, level+1, location+1, total, res)
            total -= triangle[level][location+1]
    # 法二
    # DP状态定义：dp[i, j]指从下面一层走当前层，路径和的最小值（当前层有多少点，就有多少个路径和）
    # DP状态方程：dp[i][j] = min( dp[i+1][j], dp[i+1][j+1] ) + triangle[i, j]
    # DP初始状态: dp[m-1, j] = Triangle[m-1, j]
    # 求dp[0][0]
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        level = len(triangle)
        dp = triangle[level-1]
        for i in range(level-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

    def minimumTotal(self, triangle):
        return self.minimumTotal2(triangle)


if __name__ == '__main__':
    s = Solution()
    triangle =[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    # level = len(triangle)
    # dp = triangle[level - 1]
    # print(dp)
    print(s.minimumTotal(triangle))
