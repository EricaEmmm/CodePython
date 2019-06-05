# 第k个排列
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#     给定 n 的范围是 [1, 9]。
#     给定 k 的范围是[1,  n!]。
#
# 示例 1:
# 输入: n = 3, k = 3
# 输出: "213"
#
# 示例 2:
# 输入: n = 4, k = 9
# 输出: "2314"

"""
直接用回溯法做的话需要在回溯到第k个排列时终止就不会超时了, 但是效率依旧感人
可以用数学的方法来解, 因为数字都是从1开始的连续自然数, 排列出现的次序可以推
算出来, 对于n = 4, k = 15 找到k = 15排列的过程:

1 + 对2, 3, 4的全排列(3!个)
2 + 对1, 3, 4的全排列(3!个)         3, 1 + 对2, 4的全排列(2!个)
3 + 对1, 2, 4的全排列(3!个)-------> 3, 2 + 对1, 4的全排列(2!个)-------> 3, 2, 1 + 对4的全排列(1!个)-------> 3214
4 + 对1, 2, 3的全排列(3!个)         3, 4 + 对1, 2的全排列(2!个)         3, 2, 4 + 对1的全排列(1!个)

确定第一位:
    k = 14(从0开始计数)
    index = k / (n - 1)! = 2, 说明第15个数的第一位是3
    更新k
    k = k - index * (n - 1)! = 2
确定第二位:
    k = 2
    index = k / (n - 2)! = 1, 说明第15个数的第二位是2
    更新k
    k = k - index * (n - 2)! = 0
确定第三位:
    k = 0
    index = k / (n - 3)! = 0, 说明第15个数的第三位是1
    更新k
    k = k - index * (n - 3)! = 0
确定第四位:
    k = 0
    index = k / (n - 4)! = 0, 说明第15个数的第四位是4
最终确定n = 4时第15个数为3214
"""

import math
from functools import reduce

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = []
        for i in range(n):
            nums.append(i + 1)
        k -= 1
        for i in range(n):
            factorial = math.factorial(n-i-1)   # (n-i-1)!
            index = k // factorial
            k -= index * factorial
            res += str(nums[index])
            nums = nums[:index] + nums[index+1:]
        return res


    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
    #     """
    #     res = []
    #     nums = []
    #     for i in range(n):
    #         nums.append(i+1)
    #     self.dfs(0, nums, res)
    #     tmp = [list(i) for i in res]
    #     return ''.join(str(i) for i in tmp[k-1])
    #
    # def dfs(self, start, nums, res):
    #     if start == len(nums):
    #         res.append(tuple(nums))
    #         return
    #     for i in range(start, len(nums)):
    #         nums[start], nums[i] = nums[i], nums[start]
    #         self.dfs(start+1, nums, res)
    #         nums[start], nums[i] = nums[i], nums[start]


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 5))