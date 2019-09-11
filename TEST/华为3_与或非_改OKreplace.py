# 与或非
# 优先级！>&>|；测试用例无空格；只会出现"0"，"1"，"("，")"，"&"，"|"，"!"；括号可重复嵌套
# 示例1：
# 输入：!(1&0)|0&1
# 输出：1
# 示例2：
# 输入：((!0&1))|0
# 输出：1
# 示例3：
# 输入：!(1&0)&!(!(1|0))
# 输出：1
# 示例4：
# 输入：!(1&0)&!(!(1&0))
# 输出：0

if __name__ == '__main__':
    expression = '!(1&0)&!(!(1&0))' #input()
    while len(expression) > 1:
        expression = expression.replace('!1', '0')
        expression = expression.replace('!0', '1')

        expression = expression.replace('1&1', '1')
        expression = expression.replace('1&0', '0')
        expression = expression.replace('0&1', '0')
        expression = expression.replace('0&0', '0')

        expression = expression.replace('1|1', '1')
        expression = expression.replace('1|0', '1')
        expression = expression.replace('0|1', '1')
        expression = expression.replace('0|0', '0')

        expression = expression.replace('(1)', '1')
        expression = expression.replace('(0)', '0')

    if expression == '1':
        print(1)
    else:
        print(0)