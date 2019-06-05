# 搜索二维矩阵
# 编写一个高效的算法来判断 m x n 矩阵matrix中，是否存在一个目标值target。该矩阵具有如下特性：
#     每行中的整数从左到右按升序排列。
#     每行的第一个整数大于前一行的最后一个整数。
#
# 示例 1:
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
# 示例 2:
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        if matrix == [[]]:
            return False

        row_low = 0
        row_high = len(matrix) - 1
        col_low = 0
        col_high = len(matrix[0]) - 1
        flag = 0

        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            if matrix[row_mid][col_low] > target:
                row_high = row_mid - 1
            elif matrix[row_mid][col_high] < target:
                row_low = row_mid + 1
            else:
                flag = 1
                break

        if flag:
            while col_low <= col_high:
                col_mid = (col_low + col_high) // 2
                if matrix[row_mid][col_mid] == target:
                    return True
                elif matrix[row_mid][col_mid] > target:
                    col_high = col_mid - 1
                else:
                    col_low = col_mid + 1

        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[]]
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
    print(s.searchMatrix(matrix, 13))