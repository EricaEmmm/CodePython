'''
下一个更大元素I
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
如果不存在，对应位置输出-1。
示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
'''


class Solution(object):
    # 暴力解
    # 时间复杂度：O(MN),空间复杂度：O(M)
    def nextGreaterElement1(self, nums1, nums2):
        res = []
        for i in nums1:
            flag = 0
            for j in range(len(nums2)):
                if i == nums2[j]:
                    flag = 1
                if flag and nums2[j] > i:
                    res.append(nums2[j])
                    break
            if j == len(nums2)-1 and nums2[j] <= i:
                res.append(-1)
        return res

    # 单调栈
    # 时间复杂度：O(MN),空间复杂度：O(M)
    def nextGreaterElement2(self, nums1, nums2):
        monotonicStack = [-1]
        for i in range(len(nums2)-1, -1, -1):
            2


    def nextGreaterElement(self, nums1, nums2):
        return self.nextGreaterElement2(nums1, nums2)

if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(s.nextGreaterElement(nums1, nums2))
