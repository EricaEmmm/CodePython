# 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
# 进阶:
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

class Solution(object):
    # 法一：双指针
    # 时间复杂度O(n)
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        left, right, res, sum_s = 0, 0, len(nums), 0     # 双指针都从第一位出发
        while right < len(nums):
            while sum_s < s and right < len(nums):      # sum小则右指针右移
                sum_s += nums[right]
                right += 1
            while sum_s >= s and left <= right:         # sum大则左指针右移
                res = min(res, right-left)
                sum_s -= nums[left]
                left += 1
        return res
    # 法一：二分查找
    # 时间复杂度O(nlogn)
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size_min, size_max, res = 0, len(nums), 0

        def helper(size):
            sum_sub = 0
            for i in range(len(nums)):      # O(n)
                sum_sub += nums[i]
                if i >= size:
                    sum_sub -= nums[i-size]
                if sum_sub >= s:
                    return True
            return False
        while size_min <= size_max:         # O(logn)
            mid = (size_min + size_max) // 2    # 滑动窗口大小 二分
            if helper(mid):
                res = mid
                size_max = mid - 1
            else:
                size_min = mid + 1
        return res

    def minSubArrayLen(self, s, nums):
        return self.minSubArrayLen2(s, nums)


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,2,4,3]
    print(s.minSubArrayLen(7, nums))