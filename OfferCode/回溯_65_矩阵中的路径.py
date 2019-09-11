'''
矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
a b c e
s f c s
a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
ABCEHJIG
SFCSLOPQ
ADEEMNOE
ADIDEJFM
VCEIFGGS
SGGFIECVAASABCEHJIGQEMS
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        book = [[0 for i in range(cols)] for j in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row*cols + col] == path[0]:
                    book[row][col] = 1
                    if self.helper(matrix, rows, cols, path, row, col, 1, book):
                        return True
                    book[row][col] = 0
        return False

    def helper(self, matrix, rows, cols, path, row, col, pathlen, book):
        if pathlen == len(path):
            return True
        flag = False
        if col-1 >= 0 and book[row][col-1] == 0:
            if matrix[row*cols+col-1] == path[pathlen]:
                book[row][col-1] = 1
                flag |= self.helper(matrix, rows, cols, path, row, col-1, pathlen+1, book)
                book[row][col-1] = 0
        if col+1 < cols and book[row][col+1] == 0:
            if matrix[row*cols+col+1] == path[pathlen]:
                book[row][col+1] = 1
                flag |= self.helper(matrix, rows, cols, path, row, col+1, pathlen+1, book)
                book[row][col+1] = 0
        if row-1 >= 0 and book[row-1][col] == 0:
            if matrix[(row-1)*cols+col] == path[pathlen]:
                book[row-1][col] = 1
                flag |= self.helper(matrix, rows, cols, path, row-1, col, pathlen+1, book)
                book[row-1][col] = 0
        if row+1 < rows and book[row+1][col] == 0:
            if matrix[(row+1)*cols+col] == path[pathlen]:
                book[row+1][col] = 1
                flag |= self.helper(matrix, rows, cols, path, row+1, col, pathlen+1, book)
                book[row+1][col] = 0
        return flag

if __name__ == '__main__':
    s = Solution()
    matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']#'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'#
    print(s.hasPath(matrix, 3, 4, 'bcced'))
    # a=True
    # a|=False
    # print(a)
