import random
import time

def solutionList(A, B):
    res = []
    start = time.time()
    for i in A:
        if i not in B:
            res.append(i)
    end = time.time()
    print(f'list time:{end-start}')
    return res

def solutionSet(A, B):
    res = []
    tmp = set()
    start = time.time()
    for i in A:
        tmp.add(i)
    for i in B:
        if i not in tmp:
            res.append(i)
    end = time.time()
    print(f'set time:{end-start}')
    return res

if __name__ == '__main__':
    A = random.sample(range(0,1000000000),10000); # 表示从[A,B]间随机生成N个数，结果以列表返回
    B = random.sample(range(0,1000000000),10000);

    print(solutionList(A, B))
    print(solutionSet(A, B))