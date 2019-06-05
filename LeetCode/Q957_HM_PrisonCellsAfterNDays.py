# N天后的牢房
# 8间牢房排成一排，每间牢房不是有人住就是空着。
# 每天，无论牢房是被占用或空置，都会根据以下规则进行更改：
#     如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
#     否则，它就会被空置。
# （请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）
# 我们用以下方式描述监狱的当前状态：如果第i间牢房被占用，则cell[i] == 1，否则cell[i] == 0。
# 根据监狱的初始状态，在N天后返回监狱的状况（和上述N种变化）。
#
# 示例1：
# 输入：cells = [0, 1, 0, 1, 1, 0, 0, 1], N = 7
# 输出：[0, 0, 1, 1, 0, 0, 0, 0]
# 解释：下表概述了监狱每天的状况：
# Day0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# 示例2：
# 输入：cells = [1, 0, 0, 1, 0, 0, 1, 0], N = 1000000000
# 输出：[0, 0, 1, 1, 1, 1, 1, 0]
#
# 提示：
# cells.length == 8
# cells[i]的值为0或1
# 1 <= N <= 10 ^ 9


# 数组最多256种可能，因此总会循环
# 可编程找到循环的天数,发现了14天以后一循环的规律,再取余即可
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        N = 14 if N%14 == 0 else N%14

        def helper(cells):
            tmp = [0] * 8   # 不能用tmp = cells，这是浅拷贝
            for i in range(1,7):
                tmp[i] = 1 if cells[i-1] == cells[i+1] else 0
            return tmp

        for i in range(N):
            cells = helper(cells)

        return cells


if __name__ == '__main__':
    s = Solution()
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    print(s.prisonAfterNDays(cells, 14))
