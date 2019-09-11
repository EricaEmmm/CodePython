# 给定N个非负整数，按照二进制下1的个数分类，最后有几类？
# 输入：第一行一个正整数T（表示样例个数，<10），第二行正整数N（表示数字个数，<100），第三行N个数
# 输出：几类
# 示例一：
# 输入：
# 1
# 5
# 8 3 5 7 2
# 输出：
# 3

def getOne(num):
    res = 0
    while num:
        if num & 1 == 1:
            res += 1
        num = num >> 1
    return res

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        array = list(map(int, input().split()))
        dic = {}
        for i in range(len(array)):
            tmp = getOne(array[i])
            dic[tmp] = dic.get(tmp, 0) + 1
        print(len(dic))