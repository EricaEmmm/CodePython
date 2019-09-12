'''
数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''

class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res = 1
        for i in range(abs(exponent)):
            res *= base
        return res if exponent > 0 else 1/res

if __name__ == '__main__':
    s = Solution()
    print(s.Power(2, -3))