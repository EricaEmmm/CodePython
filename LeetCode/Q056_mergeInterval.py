# 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2:
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

import tool

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if intervals == []:
            return  res
        #排序
        intervals.sort(key = lambda x : x.start)
        res.append(intervals[0])

        for i in intervals[1:]:
            if res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] # [[1,4],[2,3]] #
    tmp = tool.Interval()
    tmp.OutputIntervals(s.merge(tmp.InputIntervals(intervals)))
