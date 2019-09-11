'''
变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
f(n)=2^(n-1)
时间复杂度：O(n),空间复杂度：O(1)
'''
class Solution:
    def jumpFloorII(self, number):
        if number < 2:
            return number
        res = 1
        for i in range(number-1):
            res *= 2
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(3))
