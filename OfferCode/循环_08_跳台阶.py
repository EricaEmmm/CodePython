'''
跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
class Solution:
    # def jumpFloor(self, number):
    #     暴力递归，超时
    #     res = [0]
    #     self.helper(number, res)
    #     return res[0]
    #
    # def helper(self, number, res):
    #     if number == 0:
    #         res[0] += 1
    #         return
    #     elif number < 0:
    #         return
    #     self.helper(number-1, res)
    #     self.helper(number-2, res)

    def jumpFloor1(self, number):
        '''
        斐波那契数列：递归，记忆数组
        '''
        men = [0 for _ in range(number+1)]
        men[0] = 1
        men[1] = 2
        self.helper(number-1, men)
        return men[number-1]

    def helper(self, n, men):
        if n < 2:
            return men[n]
        if men[n] == 0:
            men[n] = self.helper(n-1, men) + self.helper(n-2, men)
        return men[n]

    def jumpFloor2(self, number):
        '''
        斐波那契数列：循环
        '''
        if number < 3:
            return number
        pre, cur = 1, 2
        for i in range(3, number+1):
            pre, cur = cur, pre + cur
        return cur

    def jumpFloor(self, number):
        return self.jumpFloor2(number)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(4))