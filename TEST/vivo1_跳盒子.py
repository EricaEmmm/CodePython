'''
n个盒子排成一行，每个盒子上有一个数字a[i]，表示该盒子上的人最多能向右移动a[i]个盒子。
小v从最左第一个盒子上开始体验游戏，最少需要移动几次能到最后一个盒子上？
输入：2 2 3 0 4
输出：2
如果没盒子或跳不到最后一个盒子上，返回-1；如果已经在最后一个盒子上，返回0。
'''

def solution(step_list):
    n = len(step_list)
    if n == 0: return -1

    res = [-1 for i in range(n)]
    res[0] = 0
    for i in range(n):
        for j in range(1, step_list[i]+1):
            if i+j < n:
                if res[i+j] == -1:
                    res[i+j] = res[i] + 1
                else:
                    res[i+j] = min(res[i+j], res[i]+1)
    return res[-1]
    pass

def solution(step_list):
    n = len(step_list)
    if n == 0: return -1

    res = [-1 for i in range(n)]
    res[0] = 0
    for i in range(n):
        for j in range(1, step_list[i]+1):
            if i+j < n:
                res[i+j] = res[i] + 1 if res[i+j] == -1 else min(res[i+j], res[i]+1)
    return res[-1]
    pass

step_list = [1,10,3] #[int(i) for i in input().split()]
print(solution(step_list))
