'''
迷宫游戏
薯队长最近在玩一个迷宫探索类游戏，迷宫是一个N*N的矩阵形状，其中会有一些障碍物禁止通过。
这个迷宫还有一个特殊的设计，它的左右边界以及上下边界是连通的，比如在(2,n)的位置继续往右走一格可以到(2,1)，
在(1,2)的位置继续往上走一格可以到(n,2)。请问薯队长从起点位置S，最少走多少格才能到达迷宫的出口位置E。
输入
第一行正整数 N。 接下来 N 行字符串。
’.’表示可以通过，’#’表示障碍物, ’S’表示起点（有且仅有一个），’E’表示出口（有且仅有一个）。
对于50%的数据0 < N < 10
对于100%的数据0 < N < 10^3
输出
输出一个整数。表示从S到E最短路径的长度, 无法到达则输出 -1
样例输入
5
.#...
..#S.
.E###
.....
.....
样例输出
4
提示
向右来到(2,5)
向右来到(2,1)
向下来到(3,1)
向右来到(3,2)
'''

if __name__ == '__main__':
    # N = int(input())
    # board = []
    # for i in range(N):
    #     tmp = input()
    #     board.append(list(tmp))
    #     if 'S' in tmp: sx, sy = i, tmp.find('S')

    N = 5
    board = [['.', '#', '.', '.', '.'],
             ['.', '.', '#', 'S', '#'],
             ['.', 'E', '#', '#', '#'],
             ['.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.']]
    sx, sy = 1, 3

    rows, cols = len(board), len(board[0])
    mark = [[0 for i in range(cols)] for j in range(rows)]
    point = [[sx, sy, 0]]
    board[sx][sy] = '#'
    while point:
        row, col, step = point.pop(0)
        if board[row][col] == 'E':
            print(step)
            break
        else:
            mark[row][col] = 1
            directions = [[row-1, col], [row, col+1], [row+1, col], [row, col-1]]
            for x, y in directions:
                if x == -1: x = cols-1
                if x == cols: x = 0
                if y == -1: y = rows-1
                if y == rows: y = 0
                if board[x][y] != '#' and mark[x][y] == 0:
                    point.append([x, y, step+1])

    if board[row][col] != 'E':
        print(-1)
