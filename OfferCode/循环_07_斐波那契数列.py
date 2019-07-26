# 斐波那契数列
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
# n<=39

# 递归
class Solution1:
    def __init__(self):
        self.array = {}
        self.array[0] = 0
        self.array[1] = 1

    def Fibonacci(self, n):
        if n < 2:
            return self.array[n]
        if self.array.get(n) is not None:
            return self.array.get(n)
        else:
            self.array[n] = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            return self.array[n]

class Solution:
    def Fibonacci1(self, n):
        """
        循环：数组存储
        时间复杂度：O(n),空间复杂度：O(n)
        """
        array = []
        array.append(0)
        array.append(1)
        for i in range(2, n+1):
            array.append(array[i-1] + array[i-2])
        return array[n]

    def Fibonacci2(self, n):
        """
        循环：变量存储
        时间复杂度：O(n),空间复杂度：O(1)
        """
        if n < 2:
            return n
        first, second = 0, 1
        for i in range(2, n+1):
            tmp = second
            second = first + second
            first = tmp
        return second

    def Fibonacci(self, n):
        return self.Fibonacci2(n)



if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(39))
