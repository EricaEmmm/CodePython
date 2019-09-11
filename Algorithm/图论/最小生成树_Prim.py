'''
给定一个n个点m条边的无向图，图中可能存在重边和自环，边权可能为负数。
求最小生成树的树边权重之和，如果最小生成树不存在则输出impossible。
给定一张边带权的无向图G=(V, E)，其中V表示图中点的集合，E表示图中边的集合，n=|V|，m=|E|。
由V中的全部n个顶点和E中n-1条边构成的无向连通子图被称为G的一棵生成树，
其中边的权值之和最小的生成树被称为无向图G的最小生成树。
输入格式
第一行包含两个整数n和m。
接下来m行，每行包含三个整数u，v，w，表示点u和点v之间存在一条权值为w的边。
输出格式
共一行，若存在最小生成树，则输出一个整数，表示最小生成树的树边权重之和，如果最小生成树不存在则输出impossible。
输入样例：
4 5
1 2 1
1 3 2
1 4 3
2 3 2
3 4 4
输出样例：
6
'''

'''
U:当前已经在联通块中的所有点的集合
1. dist[i] = inf
2. for n 次
    v <- U外离U最近的点
    利用v更新U外点到U的距离
    join[v] = true
n次迭代之后所有点都已加入到U中
平均时间复杂度：邻接矩阵:O(n^2)，邻接表+堆优化:O((m+n)logn)
'''
def prim(n, uv_dist):
    dist = [float('inf') for i in range(n+1)]   # dist[i]为顶点i到U的最短距离
    join = [False for i in range(n+1)]          # join[i]为顶点i是否以加入U
    res = 0 # 权重和
    for i in range(n):
        # 寻找离集合U最近的点v
        v = -1
        for j in range(1, n+1):
            if (not join[j]) and (v == -1 or dist[j] < dist[v]):
                v = j
        # 判断是否连通，有无最小生成树
        if i and dist[v] == float('inf'): return -1
        # 更新最新S的权值和
        if i: res += dist[v]
        join[v] = True
        # 更新U外的点到U的最短距离
        for j in range(1, n+1):
            dist[j] = min(dist[j], uv_dist[j][v])
    return res

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))

    # 邻接矩阵
    uv_dist = [[float('inf') for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        uv_dist[i][i] = 0
    for edge in edges:
        uv_dist[edge[0]][edge[1]] = uv_dist[edge[1]][edge[0]] = min(uv_dist[edge[0]][edge[1]], edge[2])

    res = prim(n, uv_dist)
    if res != -1:
        print(res)
    else:
        print('impossible')