'''
开始时，都为开；每经过t1分钟，给水管状态改变；每经过t2分钟，排水管状态改变；
给水管每分钟向泳池注入m1升水；排水管每分钟从泳池排走m2升水。
泳池最大容量m，t分钟后，泳池有几升水？
输入：第一行一个正整数T（表示样例个数，<10）；后面N行每行6个数，m、t、m1、t1、m2、t2。
输出：t分钟后泳池中水量
示例1：
输入：
5
10 2 1 5 2 5
10 2 10 5 2 5
10 2 3 5 2 5
100 100 3 4 4 3
10000 1000 10 5 5 3
输出：
0
10
2
3
2495
'''

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, t, m1, t1, m2, t2 = list(map(int, input().split()))
        res = 0
        for i in range(t):
            # 给水管状态
            if (i // t1) % 2 == 0: inp = 1
            else: inp = 0
            # 排水管状态
            if (i // t2) % 2 == 0: outp = 1
            else: outp = 0

            if inp and outp:
                res = res + m1 - m2
            elif inp and not outp:
                res += m1
            elif not inp and outp:
                res -= m2

            if res < 0:
                res = 0
            elif res > m:
                res = m
        print(res)