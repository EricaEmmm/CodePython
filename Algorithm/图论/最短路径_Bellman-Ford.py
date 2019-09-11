'''
有边数限制的最短路
给定一个n个点m条边的有向图，图中可能存在重边和自环，边权可能为负数。
请你求出从1号点到n号点的最多经过k条边的最短距离，如果无法从1号点走到n号点，输出impossible。
注意：图中可能 存在负权回路 。
输入格式
第一行包含三个整数n，m，k。
接下来m行，每行包含三个整数x，y，z，表示点x和点y之间存在一条有向边，边长为z。
输出格式
输出一个整数，表示从1号点到n号点的最多经过k条边的最短距离。
如果不存在满足条件的路径，则输出“impossible”。
输入样例：
3 3 1
1 2 1
2 3 1
1 3 3
输出样例：
3
'''

'''
1.初始化所有点将起点s到各个顶点v的距离dist(s->v)赋值为INF，dist(s->s)赋值为0。
2.进行循环，循环下标为从1到|V|-1（最多进行|V|-1轮松弛）。在循环内部，遍历所有的边，进行松弛计算：
对于每一条边e(a, b)，如果dist[a] + w(a, b) < dist[b]，则说明存在到b的更短的路径,s->…->a->b则令dist[b] = dist [a]+w(a, b)
3. 遍历都结束后，若再进行一次遍历，还能得到s到某些节点更短的路径的话，则说明存在负环路。
'''
def bellman_ford(n, m, k, edges):
    dist = [float('inf') for i in range(n+1)]   # dist[i]为源点v到顶点i的最短距离
    dist[1] = 0

    for i in range(k):  # 本来应进行进行n-1轮松弛，但要求最多经过k条边
        backup = dist[:]    # 最多只能进过k条边，所以每轮前面的松弛不能影响后面，所以备份上轮
        for j in range(m):  # 枚举每一条边
            a, b, w = edges[j]
            if backup[a] + w < dist[b]:     # 尝试对每一条边松弛
                dist[b] = backup[a] + w

    return 'impossible' if dist[n] == float('inf') else dist[n]

if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(bellman_ford(n, m, k, edges))