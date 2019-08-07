def helper(str):
    res_str = str[0]
    res_num = int(str[2:])
    return res_str, res_num

if __name__ == '__main__':
    inp = list(input().split('@')) #list('a:3,b:5,c:2@'.split('@'))#
    total = list(inp[0].split(','))
    occupy = list(inp[1].split(','))
    total_dic = {}
    for i in range(len(total)):
        tmp_str, tmp_num = helper(total[i])
        total_dic[tmp_str] = tmp_num

    if occupy[0] != '':
        for i in range(len(occupy)):
            tmp_str, tmp_num = helper(occupy[i])
            total_dic[tmp_str] -= tmp_num

    res = ''
    for i in range(len(total)):
        tmp_str, tmp_num = helper(total[i])
        if total_dic[tmp_str] != 0:
            res = res + tmp_str + ':' + str(total_dic[tmp_str]) + ','
    if len(res) != 0:
        print(res[:-1])