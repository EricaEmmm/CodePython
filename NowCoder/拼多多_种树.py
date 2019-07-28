# 种树
# 小多想在美化一下自己的庄园。他的庄园毗邻一条小河，他希望在河边种一排树，共 M 棵。
# 小多采购了 N 个品种的树，每个品种的数量是 Ai (树的总数量恰好为 M)。但是他希望任意两棵相邻的树不是同一品种的。
# 小多请你帮忙设计一种满足要求的种树方案。
# 输入描述:
# 第一行包含一个正整数 N，表示树的品种数量。
# 第二行包含 N 个正整数，第 i (1 <= i <= N) 个数表示第 i 个品种的树的数量。
# 数据范围：
# 1 <= N <= 1000
# 1 <= M <= 2000
# 输出描述:
# 输出一行，包含 M 个正整数，分别表示第 i 棵树的品种编号 (品种编号从1到 N)。
# 若存在多种可行方案，则输出字典序最小的方案。若不存在满足条件的方案，则输出"-"。
#
# 输入例子1:
# 3
# 4 2 1
# 输出例子1:
# 1 2 1 2 1 3 1

from functools import reduce

def check(tree, left):
    """
    剪枝：判断剩余坑数和任意品种树之间的关系
    :param tree: 每种树的数量
    :param left: 剩余坑数
    :return:     方案是否可行
    """
    # 若left为偶数，那么只要某品种树i的数量tree[i] > left / 2，就表示肯定种不了
    # 若left为奇数，那么只要某品种树i的数量tree[i] > left+1 / 2，就表示肯定种不了
    for i in tree[1:]:
        if i > (left+1) // 2:
            return False
    return True

def dfs(tree, ans, n, m, idx):
    """
    :param tree: 每种树的数量
    :param ans:  种树方案
    :param n:    树的品种数
    :param m:    树坑总数
    :param idx:  种到第几课
    :return:     方案是否可行
    """
    if idx == m:                # 所有坑都种满了
        return True
    if not check(tree, m-idx):  # 某品种树剩余数量大于未种坑数的一半
        return False

    for i in range(1, n+1):
        if (idx == 0) or (tree[i] > 0 and i != ans[idx-1]):
            ans.append(i)
            tree[i] -= 1
            if dfs(tree, ans, n, m, idx+1):
                return True
            ans.pop()
            tree[i] += 1
    return False

if __name__ == "__main__":
    n = int(input())
    tree = list(map(int, input().split()))
    tree.insert(0, 0)
    m = reduce(lambda x, y: x + y, tree)

    ans = []
    if dfs(tree, ans, n, m, 0):
        print(" ".join(map(str, ans)))
    else:
        print('-')
