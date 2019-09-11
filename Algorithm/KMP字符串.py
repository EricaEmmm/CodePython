'''
给定一个模式串S，以及一个模板串P，所有字符串中只包含大小写英文字母以及阿拉伯数字。
模板串P在模式串S中多次作为子串出现。
求出模板串P在模式串S中所有出现的位置的起始下标。
输入格式
第一行输入整数N，表示字符串P的长度。
第二行输入字符串P。
第三行输入整数M，表示字符串S的长度。
第四行输入字符串M。
输出格式
共一行，输出所有出现位置的起始下标（下标从0开始计数），整数之间用空格隔开。
输入样例：
3
aba
5
ababa
输出样例：
0 2
'''

'''
next[i] = j 表示下标以i-j-1为起点、i-1为终点的后缀，和下标以0为起点、j-1为终点的前缀相等，
            即p[0:j] == p[i-j-1:i]。
'''
def getNext(n, pattern):
    next = [0]*(n+1)    # next数组表示每个元素的失配位置，长度要比模板串大1
    next[0] = -1
    i, j = 0, -1
    while i < n:
        while j != -1 and pattern[i] != pattern[j]:
            j = next[j]
        i += 1
        j += 1
        next[i] = j
    return next

def findAppearance(n, pattern, m, s):
    next = getNext(n, pattern)  # next数组表示每个元素的失配位置
    i, j, res = 0, 0, []
    while i < m:                # kmp匹配（i代表模式串，j代表模板串）
        while j != -1 and s[i] != pattern[j]:
            j = next[j]
        i += 1
        j += 1
        if j == n:
            res.append(i-n) # i为完全匹配的字符串结尾下标加1，j为模板串长度
            j = next[j]
    return res


if __name__ == '__main__':
    n = int(input())
    pattern = input()
    m = int(input())
    s = input()
    print(' '.join(map(str, findAppearance(n, pattern, m, s))))
