'''
最小区间
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:
输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:
    给定的列表可能包含重复元素，所以在这里升序表示 >= 。
    1 <= k <= 3500
    -105 <= 元素的值 <= 105
'''

'''
https://www.cnblogs.com/kira2will/p/4019588.html
最小堆
用k个数组的最小值初始化大小为k的最小堆
每次删除堆顶元素，将原堆顶元素对应的数组中下一个值加入到堆中，记录最小堆的最大值和区间范围，直到某个数组都被删除
最终堆顶对应滑窗最后能取到的最小区间的左值（比它还大就不能包含这个数组了）
返回区间范围最小（相等时取最大值最小的）的区间
时间复杂度：O(NlogK)
'''

import heapq

class Solution(object):
    def smallestRange(self, nums):
        k = len(nums)
        # 初始化大小为k的最小堆
        small = []
        maxValue = -float('inf')
        for i in range(k):
            maxValue = max(nums[i][0], maxValue)
            heapq.heappush(small, (nums[i][0], i, 0))
        res = []
        # 维护最小堆
        while small:
            val, row, col = heapq.heappop(small)
            res.append((maxValue, maxValue-val))    # 记录最小堆的最大值和区间范围
            if len(nums[row]) == col+1:
                break
            else:
                heapq.heappush(small, (nums[row][col+1], row, col+1))
                maxValue = max(nums[row][col+1], maxValue)
        ans_maxValue, ans_range = float('inf'), float('inf')
        for v, r in res:
            if r < ans_range or (r == ans_range and v < ans_maxValue):
                ans_maxValue, ans_range = v, r
        return [ans_maxValue-ans_range, ans_maxValue]

if __name__ == '__main__':
    s = Solution()
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print(s.smallestRange(nums))