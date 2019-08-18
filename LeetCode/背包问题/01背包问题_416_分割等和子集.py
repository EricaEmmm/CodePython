'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:每个数组中的元素不会超过100，数组的大小不会超过200

示例1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成[1, 5, 5]和[11].

示例2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
'''


'''
问题转化：给定一个只包含正整数的非空数组，是否可以从这个数组中挑选出一些正整数，
          使得这些数的和等于整个数组元素的和的一半。
'''
class Solution(object):
    def canPartition1(self, nums):
        """
        dp[i][j]表示前i个数中部分数的和是否等于j
        状态转移：dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
        时间复杂度：O(NC)，空间复杂度：O(NC)
        """
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        mid = Sum // 2
        nums.insert(0, 0)
        dp = [[False for _ in range(mid+1)] for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1, len(nums)):
            for j in range(mid+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def canPartition2(self, nums):
        """
        dp[j]表示部分数的和是否等于j
        状态转移：dp[j] = dp[j] | dp[j-nums[i]]
        时间复杂度：O(NC)，空间复杂度：O(C)
        """
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        mid = Sum // 2
        nums.insert(0, 0)
        dp = [False for _ in range(mid+1)]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(mid, nums[i]-1, -1):
                dp[j] = dp[j] | dp[j-nums[i]]
        return dp[-1]

    def canPartition(self, nums):
        return self.canPartition2(nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 11, 5]    #[1, 2, 3, 5] #
    print(s.canPartition(nums))
