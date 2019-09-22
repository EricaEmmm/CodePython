'''
把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

import functools

class Solution:
    def PrintMinNumber(self, numbers):
        numbers = list(map(str, numbers))
        if len(numbers) < 2:
            return ''.join(numbers)
        res = sorted(numbers, key = functools.cmp_to_key(self.compare)) # python3没有cmp参数，可以用cmp_to_key转换成key用
        return ''.join(res)

    def compare(self, a, b):
        # cmp返回值必须为1，-1,0
        if a+b < b+a: return -1
        elif a+b > b+a: return 1
        else: return 0

if __name__ == '__main__':
    s = Solution()
    numbers = []
    # print(s.compare('3','2'))
    print(s.PrintMinNumber(numbers))