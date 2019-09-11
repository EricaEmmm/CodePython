
'''
中缀表达式 转 后缀表达式/逆波兰表达式
转换过程需要用到栈，具体过程如下：
    1.遇到操作数，直接输出；
    2.栈为空时，遇到运算符，入栈；
    3.遇到左括号，将其入栈；
    4.遇到右括号，执行出栈操作，并将出栈的元素输出，直到弹出栈的是左括号，左括号不输出；
    5.遇到其他运算符’+”-”*”/’时，弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈；
    6.最终将栈中的元素依次出栈，输出。
经过上面的步骤，得到的输出既是转换得到的后缀表达式。
举例：a+b*c+(d*e+f)*g ———> abc*+de*f+g*+
'''
operator_precedence = { '*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}
def infix2postfix(expression):
    stack = []
    postfix = []
    for char in expression:
        if char not in operator_precedence:
            postfix.append(char)    # 1.遇到操作数，直接输出；
        else:
            if not stack:           # 2.栈为空时，遇到运算符，入栈；
                stack.append(char)
            elif char == '(':       # 3.遇到左括号，将其入栈；
                stack.append(char)
            elif char == ')':       # 4.遇到右括号，执行出栈并将出栈的元素输出，直到弹出左括号，左括号不输出；
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            elif operator_precedence[char] > operator_precedence[stack[-1]]:
                stack.append(char)
            else:                   # 5.遇到其他运算符’+”-”*”/’时，弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈；
                while stack and operator_precedence[char] <= operator_precedence[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return postfix

'''
计算后缀表达式：
    1.如果是数字，则让其进栈
    2.若为操作符，则从栈中取出两个操作数，先取出的作为右操作数，后取出的作为左操作数，
    然后进行该操作符的运算，并使其结果入栈。
    3.重复上述过程，直至表达式扫描完成。
最终栈中只留一个元素—–>即就是结果。
'''
def calulatepostfix(postfix):
    stack = []
    for char in postfix:
        if char in operator_precedence:
            b = stack.pop()
            a = stack.pop()
            data = str(int(eval(a + char + b)))
            stack.append(data)
        else:
            stack.append(char)
    return stack[-1]

if __name__ == "__main__":
    exp = '1+3/(3+1)'  #input()
    postfix = infix2postfix(exp)
    print(calulatepostfix(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))