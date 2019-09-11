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

def find(p, x):
    # 并查集核心：查找顶点x所在树的根p[x]
    if p[x] != x:   # 如果顶点x不是根，去找根
        p[x] = find(p, p[x])
    return p[x]

'''
平均时间复杂度为O(mlogm)
'''
def kruskal(n, m, edges):
    # 按边权值从小到大排序
    edges.sort(key=lambda x:x[2])
    # 初始化根节点的并查集——n个顶点看成独立的n棵树组成的森林
    p = [i for i in range(n+1)]  # p[i]表示顶点i所在树的根
    # 逐条添加边
    res, cnt = 0, 0 # 权重和、边数
    for i in range(m):
        u, v = find(p, edges[i][0]), find(p, edges[i][1])
        if u != v:
            res += edges[i][2]
            cnt += 1
            p[u] = p[v] # 合并这两棵树
    return res if cnt == n-1 else -1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    res = kruskal(n, m, edges)
    if res != -1:
        print(res)
    else:
        print('impossible')