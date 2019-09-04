'''
笔记草稿
薯队长写了一篇笔记草稿，请你帮忙输出最后内容。
1.输入字符包括英文字符，"(" , ")" 和 "<"。
2.英文字符表示笔记内容。
3. (  ) 之间表示注释内容，任何字符都无效。 括号保证成对出现。
4. "<" 表示退格, 删去前面一个笔记内容字符。 括号不受 "<" 影响 。
输入：输入一行字符串。长度 <= 10000.
输出：输出一行字符串，表示最终的笔记内容。
示例：
输入：a<<b((c)<)
输出：b
提示：a退格删除掉了， 括号里面的c不要,  最后一个< 无效
'''

def brackets(mystring):
    res = []
    tmp_k = 0
    while mystring:
        if mystring[0] == '<':
            if res != []: res.pop()
            mystring = mystring[1:]
        elif mystring[0] == '(':
            tmp_res, tmp_k = brackets(mystring[1:])
            mystring = mystring[len(tmp_res)+tmp_k:]
        elif mystring[0] == ')':
            return res, tmp_k + 1
        else:
            res.append(mystring[0])
            mystring = mystring[1:]


if __name__ == '__main__':
    # mystring = list('<2((()))(1)<<12')   # list(input()) #
    # res = []
    # while mystring:
    #     #     if mystring[0] == '<':
    #     #         if res != []: res.pop()
    #     #         mystring = mystring[1:]
    #     #     elif mystring[0] == '(':
    #     #         tmp_res, tmp_k = brackets(mystring[1:])
    #     #         mystring = mystring[len(tmp_res)+tmp_k:]
    #     #     elif mystring[0] == ')':
    #     #         mystring = mystring[1:]
    #     #     else:
    #     #         res.append(mystring[0])
    #     #         mystring = mystring[1:]
    #     # ans = ''
    #     # for i in res:
    #     #     ans += i
    #     # print(ans)

    mystring = ('((2)1)2')  # input() #
    res = ''
    cnt = 0
    for char in mystring:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        elif char == '<' and cnt == 0 and len(res) > 0:
            res = res[:-1]
        elif char != '<' and cnt == 0:
            res += char
    print(res)


