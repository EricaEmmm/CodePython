'''
一个全部由大写字母组成的字符串，允许最多改变2个大写字母，使包含最长连续N串的长度最长。
输入：第一行一个正整数T（表示样例个数，<20），后面N行每行一个大写字符串S（<50000）
输出：最长连续N串的长度
示例1：
输入：
3
NNTN
NNNNGGNNNN
NGNNNNGNNNNNNNNSNNNN
输出：
4
10
18
'''

import string

def helper(n_str, o_str):
    res = 0
    tmp = 0
    len_o = len(o_str)
    if len_o > 1:
        for i in range(len_o - 1):
            # 三段连起来
            if len(o_str[i]) == 1 and len(o_str[i + 1]) == 1:
                tmp = len(n_str[i]) + len(n_str[i + 1]) + len(n_str[i + 2]) + 2
            # 1个点两段连起来
            elif len(o_str[i]) == 1 and len(o_str[i + 1]) > 1:
                tmp = len(n_str[i]) + len(n_str[i + 1]) + 1
            elif len(o_str[i]) > 1 and len(o_str[i + 1]) == 1:
                tmp = len(n_str[i + 1]) + len(n_str[i + 2]) + 1
            # 2个点两段连起来
            if len(o_str[i]) == 2:
                tmp = len(n_str[i]) + len(n_str[i + 1]) + 2
            if tmp > res:
                res = tmp
        # 2个点两段连起来
        if len(o_str[-1]) == 2:
            tmp = len(n_str[-1]) + len(n_str[-2]) + 2
        if tmp > res:
            res = tmp
    else:
        if len(o_str[0]) == 1:
            res = len(n_str[0]) + len(n_str[1]) + 1
        elif len(o_str[0]) == 2:
            res = len(n_str[0]) + len(n_str[1]) + 2
    return res

def fun1(s):
    up_set = set(string.ascii_uppercase) - set('N')
    for st in up_set:
        s = s.replace(st, '.')
    n_str = list(s.split('.'))
    while '' in n_str:
        n_str.remove('')
    o_str = list(s.split('N'))
    while '' in o_str:
        o_str.remove('')

    res = 0
    len_n = len(n_str)
    len_o = len(o_str)
    if len_o == 0:
        for i in range(len_n):
            tmp = len(n_str[i])
            if tmp > res:
                res = tmp
        print(res)
    elif len_n > len_o:
        res = helper(n_str, o_str)
        print(res)

    elif len_n < len_o:
        tmp = 0
        if len_o == 2:
            if len(o_str[0]) == 1 and len(o_str[-1]) == 1:
                tmp = len(n_str[-1]) + 2
                if tmp > res: res = tmp
            if len(o_str[0]) == 1:
                tmp = len(n_str[0]) + 1
                if tmp > res: res = tmp
            if len(o_str[-1]) == 1:
                tmp = len(n_str[-1]) + 1
                if tmp > res: res = tmp
            if len(o_str[0]) == 2:
                tmp = len(n_str[0]) + 2
                if tmp > res: res = tmp
            if len(o_str[-1]) == 2:
                tmp = len(n_str[-1]) + 2
                if tmp > res: res = tmp
        if tmp > res: res = tmp
        if len_o > 2:
            if len(o_str[0]) == 1 and len(o_str[1]) == 1:
                tmp = len(n_str[0]) + len(n_str[1]) + 2
            elif len(o_str[-1]) == 1 and len(o_str[-2]) == 1:
                tmp = len(n_str[-1]) + len(n_str[-2]) + 2
        if tmp > res:
            res = tmp
        if len_o > 2:
            tmp = helper(n_str, o_str[1:-1])
        if tmp > res:
            res = tmp
        print(res)
    elif len_n == len_o:
        tmp = 0
        if len_o == 1:
            if len(o_str[0]) == 1:
                tmp = len(n_str[0]) + 1
            elif len(o_str[0]) == 2:
                tmp = len(n_str[0]) + 2
            if tmp > res:
                res = tmp
        if len_o > 1:
            if len(o_str[0]) == 1 and len(o_str[1]) == 1:
                tmp = len(n_str[0]) + len(n_str[1]) + 2
            if tmp > res:
                res = tmp
            tmp = helper(n_str, o_str[1:])
        if tmp > res:
            res = tmp
        print(res)

def fun2(s):
    index = []
    lenS = len(s)
    for i in range(lenS):
        if s[i] != 'N':
            index.append(i)
    if len(index) <= 2:
        print(lenS)
        return
    res = 0
    for i in range(len(index)-1):
        l = index[i] - 1
        r = index[i+1] + 1
        while l >= 0 and s[l] == 'N':
            l -= 1
        while r < lenS and s[r] == 'N':
            r += 1
        l += 1
        r -= 1
        res = max(res, r-l+1)
    print(res)

# O(N)时间复杂度，动态规划
# 维护数组dp以及v_dp，dp保存要用到的索引，v_dp保存以当前字符结尾的最长连续字串长度(可容错2)
# 最后返回v_dp的最大值即可
def fun3(s):
  n = len(s)
  dp = [[-1, 0, 0] for _ in range(n)]
  v_dp = [0 for _ in range(n)]
  cnt = 0
  for i in range(n):
      if s[i] != 'N' and cnt == 0:
          dp[i][1] = i
          cnt += 1
      elif s[i] != 'N' and cnt == 1:
          dp[i][1] = dp[i - 1][1]
          dp[i][2] = i
          cnt += 1
      elif s[i] != 'N' and cnt == 2:
          dp[i] = dp[i - 1][1:] + [i]
      else:
          dp[i] = dp[i - 1]
      v_dp[i] = i - dp[i][0]
  print(max(v_dp))

if __name__ == '__main__':
    T = 1#int(input()) #
    for i in range(T):
        s = 'NNNNGGNNNN'#input() #
        fun3(s)


