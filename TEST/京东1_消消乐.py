'''
消消乐是当下十分火爆的一个脑力游戏。
游戏是这样的，有一个5*5的正方形网格，每个格子中有一个大于0且小于4的整数，对于一个确定的局面，
若一个格子与它上下左右四个方向的某个格子（如果存在） 数字相同，则称这两个格子是连通的，并且这种连通具有传递性。
每次，你可以选择一个格子，若与这个格子连通的格子（包括自己）数大于等于 3，你就可以选择消掉这个格子，与此同时，
与这个格子连通的所有格子会一起消失。
如果仅仅是这样，那太简单了，因为无论如何消，最后的结果都是一样的，所以我 们引入了重力系统，每次选择消掉某个格子，
并将与那个格子相连通的所有格子都消掉后将会有一些格子失去支撑，此时那些格子就会因重力而下落。
那么怎样玩才能使得最后剩下的不能消掉的格子尽量少
输入
一个5*5的矩阵描述正方形网格，数字之间用空格隔开。
输出
一个数表示最后剩下的不能消掉的格子最少是多少。
样例输入
3 1 2 1 1
1 1 1 1 3
1 1 1 1 1
1 1 1 1 1
3 1 2 2 2
样例输出
3
'''

def isConnect(array, book, cur, row, col, k, k_dic):
    if (row < 0) or (row > 4) or (col < 0) or (col > 4) or (book[row][col] != 0) or (cur != array[row][col]):
        return
    book[row][col] = k
    k_dic[k] = k_dic.get(k, 0) + 1
    isConnect(array, book, array[row][col], row-1, col, k, k_dic)
    isConnect(array, book, array[row][col], row+1, col, k, k_dic)
    isConnect(array, book, array[row][col], row, col-1, k, k_dic)
    isConnect(array, book, array[row][col], row, col+1, k, k_dic)

def color(array):
    book = [[0 for i in range(5)] for j in range(5)]
    k_dic = {}
    k = -1
    for row in range(5):
        for col in range(5):
            isConnect(array, book, array[row][col], row, col, k, k_dic)
            k -= 1
    return book, k_dic

def down(array, row, col):
    for i in range(row, 1, -1):
        array[row][col] = array[row-1][col]
    array[0][col] = -2

def clear(array, book, k_dic):
    max_v, max_k = 0, 0
    for k, v in k_dic.items():
        if max_v < v:
            max_v, max_k = v, k
    if max_v < 3:
        return False
    for row in range(5):
        for col in range(5):
            if book[row][col] == max_k:
                array[row][col] = -1
    for row in range(4,-1,-1):
        for col in range(5):
            down(array, row, col)
    return True


if __name__ == '__main__':
    # array = []
    # for i in range(5):
    #     array.append(list(map(int, input().split())))
    array =[[3, 1, 2, 1, 1],
            [1, 1, 1, 1, 3],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [3, 1, 2, 2, 2]]
    book, k_dic = color(array)
    clear(array, book, k_dic)
    print(array)