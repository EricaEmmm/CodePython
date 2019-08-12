from collections import Counter

def helper(s):
    count = 1
    str_num = []
    str = []
    for i in range(len(s)):
        if i+1 <= len(s)-1 and s[i]==s[i+1]:
            count += 1
        else:
            str_num.append(count)
            str.append(s[i])
            count = 1
    dic = Counter(s)
    count1, str1 = max(zip(dic.values(), dic.keys()))
    res = []
    for i in range(len(str)):
        if str[i] == str1:
            if i+4<= len(str) - 1 and str_num[i+1] == 1 and str[i+2] == str1 and str_num[i+3] == 1 and str[i+4] == str1:
                res.append(str_num[i] + 2 + str_num[i + 2] + str_num[i + 4])
            elif i+2 <= len(str) - 1 and str_num[i+1] == 2 and str[i+2] == str1:
                res.append(str_num[i]+2+str_num[i+2])
            elif i+2 == len(str) - 1 and str_num[i+1] == 1 and str[i+2] == str1:
                res.append(str_num[i]+1+str_num[i+2])
            else:
                res.append(str_num[i]+2)
    print(max(res))


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        helper(s)