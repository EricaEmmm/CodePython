'''
求最长的特殊子序列
现有一个长度为n的序列，需要你求出最长的子序列，使得其长度最长，并且这个子序列是满足性质C的
子序列的定义：现有1<=i1<i2...<ik<=n，ai1,ai2,...aik则为一个子序列
性质C的定义：现有子序列ai1,ai2,...aik，若ai1<=ai2<=...<=aik,则称子序列满足性质C
输入
第一行一个数n，代表序列的长度。接下来一行n个数ai，代表序列中的每个数。1≤n≤100000,1≤ai≤n
输出
一行一个数，代表最长的满足性质C的子序列的长度
样例输入
5
1 2 1 3 4
样例输出
4
'''

import random

def lis(a):
    if not a:
        return 0
    dp = [a[0]]
    for i in range(1, len(a)):
        if a[i] >= dp[-1]:
            dp.append(a[i])
        else:
            l, r = 0, len(dp)-1
            while l < r:
                mid = (l+r)//2
                if a[i] > dp[mid]:
                    l = mid +1
                else:
                    r = mid
            dp[l] = a[i]
    return len(dp)

if __name__ == '__main__':
    # n = int(input())
    # a = list(map(int, input().split()))

    a= random.sample(range(1,10),9)#[6, 7, 8, 3, 5]#[1 ,1 ,1 ,1 ,1]#[2, 8, 1, 7, 9, 5, 3, 4, 6]#
    print(a)
    print(lis(a))


