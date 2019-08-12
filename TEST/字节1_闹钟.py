'''
闹钟响时决定起不起床，起床后X分钟到达教室，上课时间为A时B分，最晚可以什么时候起床
输入：第一行N（闹钟数量），接下来N行闹钟响时间Hi（时）Mi（分），最后一行X分钟到达教室
输出：最晚起床时间
示例1：
输入：
3
5 0
6 0
7 0
59
6 59
输出：
6 0
'''

if __name__ == '__main__':
    N = 2#int(input())
    clock = [119,118]   #[]
    # for i in range(N):
    #     hour, minute = list(map(int, input().split()))
    #     time = hour*60 + minute
    #     clock.append(time)
    clock.sort()
    X = 61  #int(input())
    # hour, minute = list(map(int, input().split()))
    classTime = 3*60+0    #hour*60 + minute

    for i in range(N):
        if clock[i] + X <= classTime:
            res = clock[i]
    minute = res % 60
    hour = res // 60
    print(hour, minute)
