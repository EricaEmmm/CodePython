'''
最长上升子序列（LIS，Longest Increasing Subsequence）
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
    你算法的时间复杂度应该为 O(n^2) 。
进阶: 你能将算法的时间复杂度降低到 O(nlogn) 吗?
'''


class Solution(object):
    def lengthOfLIS1(self, nums):
        '''
        动态规划
        dp[i]表示以nums[i]为结尾的最长上升子序列长度
        时间复杂度：O(n^2)，空间复杂度：O(n)
        '''
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        maxLen = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(dp[i], maxLen)
        return maxLen

    def lengthOfLIS2(self, nums):
        '''
        优化：贪心+二分
        dp[i]表示长度为i+1的子序列尾部元素的值
        时间复杂度：O(nlogn)，空间复杂度：O(n)
        '''
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:    # 如果nums[i]大于当前dp[最长]的结尾元素，那我们把它接到后面
                dp.append(nums[i])
            else:                   # 否则就用nums[i]去替换dp数组中第一个大于等于nums[i]的元素
                l, r = 0, len(dp)-1
                while l < r:
                    mid = (l+r)//2
                    if nums[i] > dp[mid]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return len(dp)

    def lengthOfLIS(self, nums):
        return self.lengthOfLIS2(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [4,10,4,3,8,9]
    print(s.lengthOfLIS(nums))
