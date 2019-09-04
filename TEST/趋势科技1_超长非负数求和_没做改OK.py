# 超长非负数求和
# 输入：
# 1234567890123456789012345678901234567890.1234567890123456789012345678901234567890
# 1000000000100000000010000000001000000000.1000000000100000000010000000001000000000
# 输出：
# 2234567890223456789022345678902234567890.223456789022345678902234567890223456789

if __name__ == '__main__':
    a = '1234567890123456789012345678901234567890.1234567890123456789012345678901234567890'
    b = '09000000000100000000010000000001000000009.90000000001000000000100000000010000000002'
    a_int, a_dec = list(a.split('.'))
    b_int, b_dec = list(b.split('.'))

    # 小数
    res = ''
    if len(a_dec) > len(b_dec):
        res += a_dec[len(b_dec):]
        a_dec = a_dec[:len(b_dec)]
    else:
        res += b_dec[len(a_dec):]
        b_dec = b_dec[:len(a_dec)]
    # print(res,a_dec,b_dec)
    carry = 0
    for i in range(len(a_dec)-1, -1, -1):
        cur = (int(a_dec[i]) + int(b_dec[i]) + carry) % 10
        carry = (int(a_dec[i]) + int(b_dec[i]) + carry) // 10
        res = str(cur) + res
    res = '.' + res

    # 整数
    tmp = ''
    if len(a_int) > len(b_int):
        tmp += a_int[:len(a_int)-len(b_int)]
        a_int = a_int[len(a_int)-len(b_int):]
    else:
        tmp += b_int[:len(b_int)-len(a_int)]
        b_int = b_int[len(b_int)-len(a_int):]
    for i in range(len(a_int)-1, -1, -1):
        cur = (int(a_int[i]) + int(b_int[i]) + carry) % 10
        carry = (int(a_int[i]) + int(b_int[i]) + carry) // 10
        res = str(cur) + res

    for i in range(len(tmp) - 1, -1, -1):
        cur = (int(tmp[i]) + carry) % 10
        carry = (int(tmp[i]) + carry) // 10
        res = str(cur) + res
    for i in range(len(res)):
        if res[i] == '0':
            res = res[1:]
        else:
            break
    for i in range(len(res)-1, -1, -1):
        if res[i] == '0':
            res = res[:-1]
        else:
            break
    print(res)

