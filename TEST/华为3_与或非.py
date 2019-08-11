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
def comp(opt1, opt2):
    return (opt1 == '!' and opt2 in ['&', '|']) or (opt1 == '&' and opt2 == '|')

def getdata(num1, num2, opt):
    if opt == '&':
        return num1 and num2
    if opt == '|':
        return num1 or num2

def process(data, opt):
    opterator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(getdata(num1, num2, opterator))

if __name__ == '__main__':
    s = input()#'(1&0)|0&1' #input()

    data = []
    opt = []
    for i in range(len(s)):
        if s[i].isdigit():
            start = i
            while i+1 < len(s) and s[i+1].isdigit():
                i += 1
            data.append(int(s[start: i+1]))
        elif s[i] == ")":
            while opt[-1] != "(":
                process(data, opt)
            opt.pop()
        elif not opt or opt[-1] == "(" or s[i] == "(" or comp(s[i], opt[-1]):
            opt.append(s[i])
        else:
            while opt and not comp(s[i], opt[-1]):
                if opt[-1] == "(":
                    break
                process(data, opt)
                opt.append(s[i])
    while opt:
        process(data, opt)

    print(data.pop())


# ====================================================================================

operator_precedence = {
    '(': 0,
    ')': 0,
    '&': 1,
    '!': 1,
    '|': 1,
}

def postfix_convert(exp):
    stack = []
    postfix = []
    for i in range(len(exp)):
        char = exp[i]
        if char not in operator_precedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operator_precedence[char] > operator_precedence[stack[-1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[-1] == "(":
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
    while len(stack) != 0:
        postfix.append(stack.pop())
    return postfix

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_expression_tree(postfix):
    stack = []
    for char in postfix:
        if char not in operator_precedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)
    return stack.pop()

def calculate(num1, op, num2):
    if not num1.isdigit() and op =='!':
        return not num2
    if not num1.isdigit() and not num2.isdigit():
        raise ("num error")
    else:
        num1 = int(num1)
        num2 = int(num2)
    if op == "&":
        return num1 and num2
    elif op == "|":
        return num1 or num2
    else:
        raise ("op error")

def cal_expression_tree(postfix):
    stack = []
    for char in postfix:
        stack.append(char)
        if char in "|&":
            op = stack.pop()
            num2 = stack.pop()
            num1 = stack.pop()
            value = calculate(num1, op, num2)
            value = str(int(value))
            stack.append(value)
        if char in "!":
            op = stack.pop()
            num1 = stack.pop()
            value = not int(num1)
            stack.append(str(int(value)))
    return stack[0:1]

if __name__ == "__main__":
    exp = input()
    postfix = postfix_convert(exp)
    if cal_expression_tree(postfix)[0]=='1':
        print('1')
    else:
        print('0')

# ====================================================================================
def addnot(stack, num):
    if len(stack) != 0 and stack[-1] == "!":
        stack.pop()
        if int(num) == 1:
            stack.append('0')
        else:
            stack.append('1')
    else:
        stack.append(num)

def getand(stack):
    count1 = 0
    count2 = 0
    for i in range(len(stack)):
        if stack[i] == 1:
            count1 += 1
        elif stack[i] == '&':
            count2 += 1
    if count2 == 2*count1:
        return '1'
    else:
        return '0'

def helper(s, start):
    num = 0
    stack = []
    i = start
    while i < len(s) and s[i] != ')':
        if s[i].isdigit():
            num = int(s[i])
            i += 1
        elif s[i] in ['!', '&']:
            addnot(stack, num)
            stack.append(s[i])
            num = 0
            i += 1
        elif s[i] == '(':
            sums, next = helper(s, i+1)
            i = next
            stack.append(sums)
        else:
            i += 1
    addnot(stack, num)
    sums = getand(stack)
    return sums, i


if __name__ == "__main__":
    n = list(input().split('|'))
    ans = []
    for i in range(len(n)):
        k, m = helper(n[i], 0)
        ans.append(int(k))

    if sum(ans) != 0:
        print(1)
    else:
        print(0)
