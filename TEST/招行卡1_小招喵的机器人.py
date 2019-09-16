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
    s = 'RLL' #input() #
    array = list(s.split('L'))
    array = array[:-1]
    res = ''
    for i in range(len(array)):
        if len(array[i]) == 1:
            res += '11'
        elif len(array[i])%2 == 0:
            res = res + '0'*(len(array[i])-1) + str(len(array[i])//2) + str(len(array[i])//2+1)
        else:
            res = res + '0'*(len(array[i])-1) + str((len(array[i])+1)//2)*2
    print(' '.join(res))
