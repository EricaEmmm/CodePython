'''
数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution1(self, numbers):
        """
        思路：Hash
        时间复杂度：O(n),空间复杂度：O(n)
        """
        dic = Counter(numbers)
        res = 0
        for k, v in dic.items():
            if v > len(numbers) // 2:
                res = k
        return res

    def MoreThanHalfNum_Solution2(self, numbers):
        """
        思路：攻城略地，同归于尽
        时间复杂度：O(n),空间复杂度：O(1)
        """
        cnt = 0
        for i in numbers:
            if cnt == 0:
                tmp = i
                cnt += 1
            else:
                if tmp == i:
                    cnt += 1
                else:
                    cnt -= 1
        cnt = 0
        for i in numbers:
            if i == tmp:
                cnt += 1
        return 0 if cnt <= len(numbers)//2 else tmp


    def MoreThanHalfNum_Solution(self, numbers):
        return self.MoreThanHalfNum_Solution2(numbers)


if __name__ == '__main__':
    s = Solution()
    numbers = [1,2,3,2,4,2,5,2,3]
    print(s.MoreThanHalfNum_Solution(numbers))