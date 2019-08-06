def helper(item, i):
    res = ''
    j = i
    while i < len(item) and item[i] != ')':
        tmp = ''
        while i < len(item) and item[i] >= 'A' and item[i] <= 'Z':
            tmp += item[i]
            i += 1
            j += 1
        mult = 0
        while i < len(item) and  item[i] >= '0' and item[i] <= '9':
            mult = mult * 10 + int(item[i])
            i += 1
            j += 1
        if mult != 0:
            res += tmp*mult
        else:
            res += tmp
    return res, j

def dezip():
    item = input()
    n = len(item)
    res = ''
    i = 0
    while i < n:
        if item[i] == '(':
            tmp, j = helper(item, i+1)
            res += tmp
            i += j

        # if item[i] >= 'A' and item[i] <= 'Z':
        #     res += item[i]
        #     i += 1
        # elif item[i] == '(':
        #     tmp = ''
        #     j = 0
        #     while item[i+j] != ')':
        #         tmp += item[i+j]
        #         j += 1
        #     mult = 0
        #     while item[i+j] >= '0' and item[i+j] <= '9':
        #         mult = mult*10 + (item[i+j] - '0')
        #         j += 1
        #     res += tmp * mult
        #     i += j
        # # else:





def main():
    # n = int(input())
    # for i in range(n):
    #     1
    res, j = helper('AB11B)1', 1)
    print(res, j)

main()

