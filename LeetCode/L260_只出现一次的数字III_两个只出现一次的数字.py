# 只出现一次的数字 III
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 注意：
#     结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
#     你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？


class Solution(object):
    """
    法一：HashMap
    时间复杂度：O(n)，空间复杂度：O(n)
    """
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1  # 返回指定键的值，如果值不在字典中返回default值
        for k, v in hash.items():
            if v == 1:
                res.append(k)
        return res

    """
    法一：异或
    时间复杂度：O(n)，空间复杂度：O(1)
    """
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 求全部数异或结果
        total_xor = 0
        for i in nums:
            total_xor ^= i

        # 求异或结果中非零的最低位
        index = 0
        while total_xor & 1 == 0:
            total_xor = total_xor >> 1
            index += 1

        # 将原数组分成两个子数组，且刚好每个子数组中各自包含一个只出现一次的数字
        nums1, nums2 = 0, 0
        for i in nums:
            if (i >> index) & 1 == 1:
                nums1 ^= i
            else:
                nums2 ^= i

        return [nums1, nums2]

    def singleNumber(self, nums):
        return self.singleNumber2(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1,3,2,5]
    print(s.singleNumber(nums))
