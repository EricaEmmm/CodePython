'''
俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
说明:不允许旋转信封。
示例:
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
'''

class Solution(object):
    def maxEnvelopes1(self, envelopes):
        '''
        动态规划：超时
        dp[i]表示以envelopes[i][1]为结尾的最长上升子序列长度
        时间复杂度：O(n^2)，空间复杂度：O(n)
        '''
        # 特判
        if not envelopes:
            return 0
        # 对第一列排序，按照宽度排序
        envelopes.sort(key = lambda x:x[0])
        # 以 envelopes[i][1] 结尾的上升子序列的长度
        dp = [1 for _ in range(len(envelopes))]
        maxLen = 0
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(maxLen, dp[i])
        return maxLen

    def maxEnvelopes2(self, envelopes):
        '''
        优化：贪心+二分
        dp[i]表示长度为i+1的子序列尾部元素的值
        时间复杂度：O(nlogn)，空间复杂度：O(n)
        '''
        # 特判
        if not envelopes:
            return 0
        # 信封宽度一样时，让高度降序排列：
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        nums = [x[1] for x in envelopes]
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]> dp[-1]:
                dp.append(nums[i])
            else:
                l, r = 0, len(dp)-1
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return len(dp)

    def maxEnvelopes(self, envelopes):
        return self.maxEnvelopes2(envelopes)

if __name__ == '__main__':
    s = Solution()
    envelopes = [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]#[[5,4],[6,4],[6,7],[2,3]]#[[30,50],[12,2],[3,4],[12,15]]#
    print(s.maxEnvelopes(envelopes))
