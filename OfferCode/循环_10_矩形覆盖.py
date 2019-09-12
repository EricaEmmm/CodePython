'''
矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''


'''
斐波那契数列变种
f(1)=1
f(2)=2
f(3)=最后一竖着放f(2)+最后一横着放f(1)
f(n)=f(n-1)+f(n-2)
时间复杂度：O(n),空间复杂度：O(1)
'''
class Solution:
    def rectCover(self, number):
        if number < 3:
            return number
        pre = 1
        cur = 2
        for i in range(2, number):
            cur = cur + pre
            pre = cur - pre
        return cur

if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(3))