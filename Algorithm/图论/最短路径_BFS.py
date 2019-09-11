'''
走迷宫
给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。
最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。
请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。
数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。
输入格式
第一行包含两个整数n和m。
接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。
输出格式
输出一个整数，表示从左上角移动至右下角的最少移动次数。
输入样例：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8
'''

def bfs(n, m, board):
    mark = [[0 for i in range(m)] for j in range(n)]
    point = [[0, 0, 0]]
    while point:
        row, col, step = point.pop(0)
        if row == n-1 and col == m-1:
            return step
        else:
            mark[row][col] = 1
            directions = [[row-1, col], [row, col+1], [row+1, col], [row, col-1]]
            for x, y in directions:
                if 0 <= x < n and 0 <= y < m and board[x][y] == 0 and mark[x][y] == 0:
                    point.append([x, y, step+1])
    return -1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    print(bfs(n, m, board))