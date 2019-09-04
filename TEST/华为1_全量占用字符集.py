# 输入为一个字符串，包含全量字符集和已占用字符集，两字符集用@连接。已占用字符集一定是全量字符集中的字符。
# 输出可用字符集，输出带回车换行。
# 注：输出字符顺序要与输入一致；如果某个字符已被占用，不要再输出。
# 示例1：
# 输入：a:3,b:5,c:2@a:1,b:2
# 输出：a:2,b:3,c:2
# 示例2：
# 输入：a:3,b:5,c:2@a:3,b:2
# 输出：b:3,c:2

def helper(str):
    res_str = str[0]
    res_num = int(str[2:])
    return res_str, res_num

def solve(total, occupy):
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

if __name__ == '__main__':
    inp = list(input().split('@')) #list('a:3,b:5,c:2@'.split('@'))#
    total = list(inp[0].split(','))
    occupy = list(inp[1].split(','))
    solve(total, occupy)