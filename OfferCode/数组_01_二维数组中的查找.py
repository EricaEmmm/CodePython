# 二维数组中的查找
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        rowm = len(array)
        if rowm == 0:
            return False
        coln = len(array[0])
        if coln == 0:
            return False

        row, col = 0, coln-1
        while row < rowm and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            elif array[row][col] < target:
                row += 1
        return False



if __name__ == '__main__':
    s = Solution()
    matrix = [ ]
    #     [1,2,8,9],
    #     [2,4,9,12],
    #     [4,7,10,13],
    #     [6,8,11,15]
    # ]
    print(s.Find(14, matrix))
