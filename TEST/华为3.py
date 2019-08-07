
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
