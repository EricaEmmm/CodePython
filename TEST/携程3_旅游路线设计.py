'''
旅游路线设计 TSP问题
用户出行旅游通常都是一个闭环，即从某地出发游览各个景点，最终回到出发地。
已知各个景点间的通行时间。请你设计一套算法，当用户给定出发地以及景点后，给出一条游览路线，
使得用户能够不重复的游历每个景点并返回出发地的总通行时间最短，计算该最短通行时间。假设所有用户的出发地都是0
输入
第一行：出发地与景点的总个数 n
第二行：景点间的直达路线的个数m
其后m行：各个景点的通行时间a   b   t
表示a地与b地之间的通行时间是t。
输出
不重复游览完所有景点并返回出发地的最短游览时间T
若不存在这样的游览路线，返回-1
样例输入
4
6
0 1 4
0 2 3
0 3 1
1 2 1
1 3 2
2 3 5
样例输出
7
'''
def find_path(j):
    path_vertexs.append(j)  #把该节点标记为已走过
    row=c[j]
    #创建copy_row,删除row中已走过的顶点,防止直接在row上操作.
    copy_row=[value for value in row]
    walked_vertex=[]
    for i in path_vertexs:#已走过的顶点
        walked_vertex.append(copy_row[i])
    for vertex in walked_vertex:
        copy_row.remove(vertex)
    #寻找row中的未遍历过的最短边
    if len(path_vertexs)<n:
        min_e=min(copy_row)
        j=row.index(min_e)
        path_length.append(min_e)
        find_path(j)
    else:
        min_e=c[j][0]
        path_length.append(min_e)
        path_vertexs.append(0)
    return path_length

if __name__ == "__main__":
    n=int(input())
    m=int(input())
    c=[[0]*n for _ in range(n)]
    for i in range(m):
        x,y,time=list(map(int,input().split()))
        c[x][y]=time
        c[y][x] = time
    path_length=[]
    path_vertexs=[]
    path_length=find_path(0)
    print(sum(path_length))