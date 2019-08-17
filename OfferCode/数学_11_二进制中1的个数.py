'''
二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1_1(self, n):
        # 某数减1再和原数做与，可以消掉二进制最右边一个1
        cnt = 0
        if n < 0:
            n = n & 0xffffffff  # Python中的整型以补码形式存储，十进制负数以其正数原码的二进制表示加上个负号，获得负数补码要&0xffffffff！！！！
        while n != 0:
            cnt += 1
            n = n & (n-1)
        return cnt
    def NumberOf1_2(self, n):
        # 右移
        cnt = 0
        if n < 0:
            n = n & 0xffffffff  # Python中的整型以补码形式存储，十进制负数以其正数原码的二进制表示加上个负号，获得负数补码要&0xffffffff！！！！
        while n != 0:
            if n&1 == 1:
                cnt += 1
            n = n >> 1
        return cnt

    def NumberOf1(self, n):
        return self.NumberOf1_2(n)

if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(10))
