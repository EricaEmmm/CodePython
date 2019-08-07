operator_precedence = {
    '(':0,
    ')':0,
    '&': 1,
    '|': 1,
    '!': 1,
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
            node.left = left
            node.right = right
            stack.append(node)
    return stack.pop()

def cal(num1, op, num2):
    if not num1.isdigit() and op == '!':
        return not num2
    if not num1.isdigit() and not num2.isdigit():
        raise("num error")
    else:
        num1 = int(num1)
        num2 = int(num2)
    if op == "&":
        return num1 and num2
    if op == "|":
        return num1 or num2

def cal_ex(postfix):
    stack=[]
    for char in postfix:
        stack.append(char)
        if char in "|&":
            op = stack.pop()
            num2=stack.pop()
            num1=stack.pop()
            value=cal(num1,op,num2)
            value=str(value)
            stack.append(value)
        if