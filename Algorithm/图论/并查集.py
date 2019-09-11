'''
一共有n个数，编号是1~n，最开始每个数各自在一个集合中。
现在要进行m个操作，操作共有两种：
    “M a b”，将编号为a和b的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
    “Q a b”，询问编号为a和b的两个数是否在同一个集合中；
输入格式
第一行输入整数n和m。
接下来m行，每行包含一个操作指令，指令为“M a b”或“Q a b”中的一种。
输出格式
对于每个询问指令”Q a b”，都要输出一个结果，如果a和b在同一集合内，则输出“Yes”，否则输出“No”。
每个结果占一行。
输入样例：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
输出样例：
Yes
No
Yes
'''

class UnionFindSet:
    def __init__(self, nodes):
        '''
        初始化parent数组
        parent[i]：索引为i的节点，它的直接父节点为parent[i]
        '''
        self.parent = nodes

    def get_root(self, node):
        '''
        找到当前节点的根
        每次查询都会优化
        只有根节点的父节点是自己
        若当前节点的直接父节点不为根节点，就递归地将自己的父节点设置为根节点
        '''
        if self.parent[node] != node:
            self.parent[node] = self.get_root(self.parent[node])
        return self.parent[node]

    def is_connected(self, i, j):
        '''
        判断两节点是否连通
        '''
        return self.get_root(i) == self.get_root(j)

    def union(self, i, j):
        '''
        两集合合并
        并非让两节点自身相连，是让它们所属的集合实现合并
        '''
        i_root = self.get_root(i)
        j_root = self.get_root(j)
        self.parent[i_root] = j_root

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    myset = UnionFindSet(list(range(n+1)))
    order, a, b = ['' for _ in range(m)], ['' for _ in range(m)], ['' for _ in range(m)]
    for i in range(m):
        order[i], a[i], b[i] = list(input().split())

    for i in range(m):
        if order[i] == 'M':
            myset.union(int(a[i]), int(b[i]))
        if order[i] == 'Q':
            if myset.is_connected(int(a[i]), int(b[i])): print('Yes')
            else: print('No')