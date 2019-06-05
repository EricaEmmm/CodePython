# 最小面积矩形
# 给定在xy平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于x轴和y轴。
# 如果没有任何矩形，就返回0。
#
# 示例1：
# 输入：[[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
# 输出：4
#
# 示例2：
# 输入：[[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
# 输出：2
#
# 提示：
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        if n < 4:
            return res

        mem = set()
        for x1, y1 in points:
            for x2, y2 in mem:
                if (x1, y2) in mem and (x2, y1) in mem:
                    if not res:
                        res = abs(x2-x1)*abs(y2-y1)
                    else:
                        res = min(res, abs(x2-x1)*abs(y2-y1))
            mem.add((x1, y1))

        return res

if __name__ == '__main__':
    s = Solution()
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    print(s.minAreaRect(points))

    # t = []
    # for i, j in points:
    #     print([i,j])

    # a = set('abcd')
    # a = set(['a', 'b', 'c', 'd'])
    # a = set({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    # print(a)