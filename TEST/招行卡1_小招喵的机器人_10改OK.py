'''
一根数轴上，1~n的每个点都标有L或R，最初每个点有一个机器人。所有机器人一起执行10^100次：
若该点有L，则机器人左移；若该点有R，则机器人右移。
保证点1为R，点n为L。最后，每个点上有几个机器人？
输入：一行字符串s，表示每个点的标记
输出：一行每个点的机器人数量
2<=|s|<=10^5
示例一：
输入：RRLRL
输出：0 1 2 1 1
示例二：
输入：RRRRRLRLRL
输出：0 0 0 0 3 3 1 1 1 1
'''

if __name__ == '__main__':
    s = 'RRLRL' #input() #
    res = [0 for i in range(len(s))]
    for i in range(len(s)):
        if s[i] == 'R':
            j = 0
            while s[i+j] == 'R':
                j += 1
            if j % 2 == 1:
                res[i+j-1] += 1
            else:
                res[i+j] += 1
        elif s[i] == 'L':
            j = 0
            while s[i-j] == 'L':
                j += 1
            if j % 2 == 1:
                res[i-j+1] += 1
            else:
                res[i-j] += 1

    print(' '.join(map(str, res)))