'''
骰子期望
扔n个骰子，第i个骰子可能有Xi种等概率的结果，数字从1~Xi。
所有骰子结果的最大值将作为最终结果，求最终结果期望。
输入：第一行一个整数n（骰子数），第二行n个整数（每个骰子的结果数Xi）
输出：最终结果的期望（保留两位有效数字）
示例:
输入：
2
2 2
输出
1.75
'''


def backtrack(X, track, res):
    if len(X) == 0:
        res.append(max(track))
        return
    for j in range(1, X[0] + 1):
        track.append(j)
        backtrack(X[1:], track[:], res)
        track = track[:-1]

if __name__ == '__main__':
    # n = int(input())
    # X = list(map(int, input().split()))
    n = 2
    X = [2,2]

    from functools import reduce
    all = reduce(lambda x, y: x * y, X)

    res = []
    backtrack(X[:], [], res)
    print('%.2f' % (sum(res)/all))