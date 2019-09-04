'''
扫雷游戏
给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，
'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），
根据以下规则，返回相应位置被点击后对应的面板：
    如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
    如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
    如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
    如果在此次点击中，若无更多方块可被揭露，则返回面板。
示例 1：
输入:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''

class Solution(object):
    def updateBoard1(self, board, click):
        '''
        BFS
        '''
        if not board:
            return board
        point = [click]
        rows, cols = len(board), len(board[0])
        mark = [ [0 for i in range(cols)] for j in range(rows) ]
        while point:
            row, col = point.pop(0)
            if mark[row][col] == 0:
                if board[row][col] == 'M':  # 一下就挖到地雷，可以直接修改然后返回
                    board[row][col] = 'X'
                    return board
                else:
                    mark[row][col] = 1
                    cnt = 0
                    directions = [[row, col-1], [row+1, col-1], [row+1, col], [row+1, col+1],
                                  [row, col+1], [row-1, col+1], [row-1, col], [row-1, col-1]]
                    for x, y in directions:
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'M':
                            cnt += 1
                    if cnt: # 如果有雷，就直接说有几个雷
                        board[row][col] = str(cnt)
                    else:   # 没有相邻地雷，就还需要搜索周围的点
                        board[row][col] = 'B'
                        for x, y in directions:
                            if 0 <= x < rows and 0 <= y < cols and mark[x][y] == 0:
                                point.append([x, y])
        return board

    def updateBoard2(self, board, click):
        '''
        DFS
        '''
        if not board:
            return board
        rows, cols = len(board), len(board[0])
        mark = [ [0 for i in range(cols)] for j in range(rows) ]
        def dfs(board, click, mark):
            row, col = click
            if mark[row][col] == 0:
                if board[row][col] == 'M':  # 一下就挖到地雷，可以直接修改然后返回
                    board[row][col] = 'X'
                    return
                else:
                    mark[row][col] = 1
                    cnt = 0
                    directions = [[row, col-1], [row+1, col-1], [row+1, col], [row+1, col+1],
                                  [row, col+1], [row-1, col+1], [row-1, col], [row-1, col-1]]
                    for x, y in directions:
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'M':
                            cnt += 1
                    if cnt: # 如果有雷，就直接说有几个雷
                        board[row][col] = str(cnt)
                    else:   # 没有相邻地雷，就还需要搜索周围的点
                        board[row][col] = 'B'
                        for x, y in directions:
                            if 0 <= x < rows and 0 <= y < cols and mark[x][y] == 0:
                                dfs(board, [x, y], mark)
        dfs(board, click, mark)
        return board

    def updateBoard(self, board, click):
        return self.updateBoard2(board, click)

if __name__ == '__main__':
    s = Solution()
    board = [
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    print(s.updateBoard(board, click))

