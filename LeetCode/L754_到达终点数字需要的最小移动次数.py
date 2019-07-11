# 到达终点数字
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
# 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
# 返回到达终点需要的最小移动次数。
#
# 示例 1:
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#
# 示例 2:
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
#
# 注意:
#     target是在[-10^9, 10^9]范围中的非零整数。


"""
由于对称性 target是正或负不影响，都取正。
假设1+2+3+...+k=sum
1、如果sum=target，最终答案是k
2、如果sum-target为偶数，最终答案是k
    1+...-（sum-target）/2+...+k = target
 => sum - (sum-target) = target
 => 1+2....+k减去了sum-target
3、如果sum-target为奇数，k是偶数，最终答案是k+1
    1+...-(sum-target+1)/2+....-(k/2)...+k+(k+1) = target
 => sum+(k+1) - (sum-target+1) - k = target
 => 1+2....+k+(k+1)减去了sum-target+1和k
4、如果sum-target为奇数，k是奇数，最终答案是k+2
    1+2+...-(sum-target+1)/2.....+k-(k+1)+(k+2) = target
 => sum-(k+1)+(k+2) - (sum-target+1) = target
 => sum+1 - (sum-target+1) = target
 => 1+2....+k-(k+1)+(k+2)减去了sum-target+1
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        point, step = 0, 0
        target = abs(target)
        while point < target:
            step += 1
            point += step

        if (point-target)%2 == 0:
            return step
        else:
            if step%2 == 0:
                return step+1
            else:
                return step+2


if __name__ == '__main__':
    s = Solution()
    print(s.reachNumber(3))



