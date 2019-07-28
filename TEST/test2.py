if __name__ == '__main__':
    strings = list(input().split())
    n = len(strings)
    # print(strings)

    dic_head = {}
    res = []
    for i in range(n):
        dic_head[strings[i][0]] = i     # 键：字符串头，值：字符串位置

    tail = strings[0]
    res.append(0)
    for i in range(1, n):
        tmp = dic_head.get(tail[-1])    # 字符串位置
        if tmp != None:
            res.append(tmp)
            dic_head.pop(tail[-1])
            tail = strings[tmp]

    if len(res) != n:
        print(False)
    else:
        print(True)