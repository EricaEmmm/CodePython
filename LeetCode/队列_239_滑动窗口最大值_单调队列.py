'''
滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
进阶：
你能在线性时间复杂度内解决此题吗？
'''

'''
复杂度分析
暴力：遍历每个滑窗
    时间：O(NK)，空间：O(N-k+1)
最大堆：维护堆顶
    时间：O(Nlogk)，空间：O(k)
单调队列：比较环节用优先队列（最小堆）优化，比较代价O(logK)
    时间：O(NlogK)，空间：O(K)
双向队列：将K个链表一直对半分，向上两两合并。每次合并都要遍历几乎全部N个节点，合并logK次
    时间：O(NlogK)，空间：O(NlogK)
'''
class monotonicQueue(object):
    # 保证队列中元素单调递减
    def __init__(self):
        self.data = []

    # 队尾添加元素，要把前面比新元素小的元素都删掉
    def push(self, n):
        while self.data != [] and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    # 返回最大值，即队首
    def max(self):
        if self.data == []:
            return None
        else:
            return self.data[0]

    # 删除队首
    def pop(self, n):
        if self.data[0] == n:
            del self.data[0]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        monQue = monotonicQueue()
        for i in range(k):
            monQue.push(nums[i])
        if monQue.max():
            res = [monQue.max()]
        else:
            res = []
        for i in range(k, len(nums)):
            monQue.pop(nums[i-k])
            monQue.push(nums[i])
            res.append(monQue.max())
        return res

if __name__ == '__main__':
    s = Solution()
    nums = []
    k = 0
    print(s.maxSlidingWindow(nums, k))