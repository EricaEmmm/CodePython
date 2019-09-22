'''
报数
将N（<1000）个人排一排，从第一个开始报数，如果是M的倍数就出列，报到队尾则从队头继续报，
直到所有人都出列；
输入描述：N M
输出描述：int数组，每个数表示原来在队列中的位置，空格隔开
示例：
输入：6 3
输出：3 6 4 2 5 1
'''

def same(person, l, n):
    for i in range(l):
        if person[i] == n:
            return True
    return False

def solution(N, M):
    person = [0 for i in range(N)]
    cnt = 1
    res = []
    while True:
        if cnt > N * M:
            break
        for i in range(1, N+1):
            while True:
                if same(person, N, i) == False:
                    break
                else:
                    i += 1
            if i > N:
                break
            if cnt % M == 0:
                res.append(str(i))
                person[cnt//M-1] = i
            cnt += 1
    print(' '.join(res))
    pass

# 约瑟夫环
def solution1(N, M):
    people = list(range(1, N + 1))
    ans = []
    while len(people) > 0:
        i = 1  # 每次while循环时初始化i
        while i < M:
            people.append(people.pop(0))
            i += 1
        ans.append(str(people.pop(0)))
    print(' '.join(ans))
    pass

N, M = [int(i) for i in input().split()]
solution1(N, M)