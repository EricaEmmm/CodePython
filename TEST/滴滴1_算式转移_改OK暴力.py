'''
给出仅包含加减乘除的算式，保持运算符顺序不变时，若交换相邻两个数且表达式值不变，则可交换。
经过任意次操作，使数字字典序最小。
输入：第一行为整数n（算式长度），第二行为n个数字和n-1个字符
输出：字典序最小的表达式
示例：
输入：
6
3 + 2 + 1 + -4 * -5 + 1
输出：
1 + 2 + 3 + -5 * -4 +1
'''


if __name__ == '__main__':
    # n = int(input())
    # expression = list(input().split(' '))
    n = 4
    expression = '3 - 2 / 8 / -1'  #'3 + 2 + 1 + -4 * -5 + 1'#
    expression = list(expression.split(' '))

    nums = list(map(int, expression[::2]))
    opts = expression[1::2]

    res = []
    num_que = [nums.pop(0)]
    opt_que = []
    while opts != []:
        opt, num = opts.pop(0), nums.pop(0)
        if opt_que == []:
            if opt == '-' or opt == '/':
                res.extend(num_que)
                num_que = []
            num_que.append(num)
            opt_que.append(opt)
        elif opt == opt_que[-1]:
            num_que.append(num)
            opt_que.append(opt)
        else:
            if opt_que[-1] == '+':
                if opt == '-':
                    res.extend(sorted(num_que))
                    num_que = [num]
                elif opt == '*':
                    res.extend(sorted(num_que[:-1]))
                    num_que = [num_que[-1]]
                    num_que.append(num)
                elif opt == '/':
                    res.extend(sorted(num_que[:-1]))
                    res.append(num_que[-1])
                    num_que = [num]
            elif opt_que[-1] == '-':
                if opt == '+':
                    res.extend(sorted(num_que))
                    num_que = [num]
                elif opt == '*':
                    res.extend(sorted(num_que[:-1]))
                    num_que = [num_que[-1]]
                    num_que.append(num)
                elif opt == '/':
                    res.extend(sorted(num_que[:-1]))
                    res.append(num_que[-1])
                    num_que = [num]
            elif opt_que[-1] == '*' or opt_que[-1] == '/':
                    res.extend(sorted(num_que))
                    num_que = [num]
            opt_que.append(opt)
    res.extend(sorted(num_que))


    # for i in range(n-1):
    #     if i == n-2:
    #         if (opts[i] == '+') or (opts[i] == '*'):
    #             nums[i - cnt:i] = sorted(nums[i - cnt:i])
    #         elif (opts[i] == '-') or (opts[i] == '/'):
    #             nums[i - cnt + 1:i] = sorted(nums[i - cnt + 1:i])
    #     if not tmp or opts[i] != tmp:
    #         if (tmp == '+' and opts[i] == '-') or (tmp == '*'):
    #             nums[i-cnt:i+1] = sorted(nums[i-cnt:i+1])
    #         elif (tmp == '+'):
    #             nums[i-cnt:i] = sorted(nums[i-cnt:i])
    #         elif (tmp == '-' and opts[i] == '+') or (tmp == '/'):
    #             nums[i-cnt+1:i+1] = sorted(nums[i-cnt+1:i+1])
    #         elif (tmp == '-'):
    #             nums[i-cnt+1:i] = sorted(nums[i-cnt+1:i])
    #         cnt = 1
    #         tmp = opts[i]
    #     else:
    #         cnt += 1

    ans = str(res[0])
    for i in range(1, n):
        ans = ans + ' ' + opt_que[i-1] + ' ' + str(res[i])
    print(ans)

