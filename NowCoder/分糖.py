# while True:
#     try:
#
#     except:
#         break

#
# #输入是单个数
# h_num=input()
# #输入是数组转换成list
# h = list(map(int,input().split()))
import random
print(random.randint(3,45))
print(random.randrange(3,45,1))
print(random.random( ))
print(random.uniform(1,2))

import sys
N=int(sys.stdin.readline().strip())
ai_list=list(map(int,sys.stdin.readline().split()))
K,D=list(map(int,sys.stdin.readline().split()))




#不用sys
n, m = map(int, input().split())
mave = []
for i in range(n):
    mave.append(input().strip())#去头尾空格
x0, y0 = map(int, input().split())
k = int(input())
directions = []
for i in range(k):
    directions.append(tuple(map(int, input().split())))
    directions.append(list(map(int, input().split())))




import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))




#解答
def solve(n, m, mave, x0, y0, k, directions):

if __name__ == '__main__':
    #输入
    n, m = map(int, input().split())    # 通过指定分隔符对字符串进行切片,
    mave = []
    for i in range(n):
        mave.append(input().strip())  # 去头尾空格
    x0, y0 = map(int, input().split())
    k = int(input())
    directions = []
    for i in range(k):
        directions.append(tuple(map(int, input().split())))
        directions.append(list(map(int, input().split())))
    #把输入全部传去
    res=solve()
    #输出
    print(res)