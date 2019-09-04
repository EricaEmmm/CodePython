'''
前缀树查找
Trie树：
圆圈表示内部节点，指向孩子节点的每个标记的值范围在0-255之间，每个内部节点最多有256个孩子节点。
三角形表示叶子节点，每个叶子节点存储一个value，根节点到叶子节点之间路径上的所有字符构成完整key。
Trie树可以采用post order unary degree sequence（POUDS）进行唯一编码。
现有一颗用pouds编码的Trie数，树中key长度均相同，输入要查找的key，输出对应的value。
输入：
第1行，数字M表示labels、haschild、pouds数组大小
紧跟着3行，分别表示labels、haschild、pouds数组内容
第5行，数字N表示values数组大小；第6行，表示values数组内容
第7行，数字P表示key数组大小；第8行，表示要查找的key字符数组
输出：
一行key对应的value，若可以不存在则输出0
示例：
输入：
15
115 112 116 97 111 121 114 101 105 112 121 114 102 115 116
0 0 0 1 1 0 1 0 0 0 0 1 1 1 1
1 1 0 1 0 1 1 1 0 0 0 1 1 0 0
8
1 2 3 4 5 6 7 8
3
116 114 112
输出：
7
'''

if __name__ == '__main__':
    M = input(input())
    labels = list(map(int, input().split()))
    haschild = list(map(int, input().split()))
    pouds = list(map(int, input().split()))
    N = input(input())
    values = list(map(int, input().split()))
    P = input(input())
    key = list(map(int, input().split()))

