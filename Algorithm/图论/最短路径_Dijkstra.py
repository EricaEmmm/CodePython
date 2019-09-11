'''
给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为正值。
请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。
输入格式
第一行包含整数n和m。
接下来m行每行包含三个整数x，y，z，表示点x和点y之间存在一条有向边，边长为z。
输出格式
输出一个整数，表示1号点到n号点的最短距离。
如果路径不存在，则输出-1。
输入样例：
3 3
1 2 2
2 3 1
1 3 4
输出样例：
3
'''

'''
S:已求出最短路径的顶点集合
U:其余未确定最短路径的顶点集合
1. dist[1] = 0，dist[i] = inf
2. for n 次
    k <- U中距离源点v最近的点
    利用k更新U中点到源点v的距离
    join[k] = true
n次迭代之后所有点都已加入到S中
'''
# 邻接矩阵存储
# 平均时间复杂度：O(n^2)
def dijkstra1(n, m):
    # 构建邻接矩阵
    xy_dist = [[float('inf') for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        xy_dist[i][i] = 0
    for i in range(m):
        x, y, z = list(map(int, input().split()))
        xy_dist[x][y] = min(xy_dist[x][y], z)

    dist = [float('inf') for i in range(n+1)]   # dist[i]为源点v到顶点i的最短距离
    join = [False for i in range(n+1)]          # join[i]为顶点i是否以加入S
    dist[1] = 0
    for i in range(n-1):
        # 寻找离源点v最近的点k
        k = -1
        for j in range(1, n+1):
            if (not join[j]) and (k == -1 or dist[j] < dist[k]):
                k = j
        join[k] = True
        # 利用k更新U中点到源点v的距离
        for j in range(2, n+1):
            dist[j] = min(dist[j], dist[k]+xy_dist[k][j])

    return -1 if dist[n] == float('inf') else dist[n]


# 邻接表存储+堆优化
# 平均时间复杂度：O((m+n)logn)
def add(x, y, z, h, e, ne, w, idx):
    e[idx], w[idx], ne[idx], h[x] = y, z, h[x], idx

def dijkstra2(n, m):
    # 构建邻接表
    h, e, ne, w, idx = [-1]*(max(m, n)+1), [0]*(max(m, n)+1), [0]*(max(m, n)+1), [0]*(max(m, n)+1), 0
    for i in range(m):
        x, y, z = list(map(int, input().split()))
        add(x, y, z, h, e, ne, w, idx)
        idx += 1

    join = [False for i in range(n+1)]          # join[i]为顶点i是否以加入S
    join[1] = True
    dist = [float('inf') for i in range(n+1)]   # dist[i]为源点v到顶点i的最短距离
    dist[1] = 0

    from queue import PriorityQueue
    smallheap = PriorityQueue() # 最小堆存储(节点u到源点v的距离, 节点u)
    smallheap.put((dist[1], 1))

    while not smallheap.empty():
        vk_dist, k = smallheap.get()
        join[k] = True
        i = h[k]
        while i != -1:
            j = e[i]
            if dist[j] > vk_dist+w[i]:
                dist[j] = vk_dist+w[i]
                smallheap.put((dist[j], j))
            i = ne[i]

    return -1 if dist[n] == float('inf') else dist[n]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    print(dijkstra2(n, m))
