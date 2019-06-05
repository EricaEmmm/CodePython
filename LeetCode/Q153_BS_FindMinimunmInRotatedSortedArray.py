# 寻找旋转排序数组中的最小值
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2:
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]:  #没有旋转
            return nums[0]

        while left < right:
            if right - left == 1:
                break
            mid = (left + right) // 2
            if nums[left] > nums[mid]:      #最小值在左边
                right = mid
            elif nums[right] < nums[mid]:   #最小值在右边
                left = mid

        return (nums[left] if nums[left] < nums[right] else nums[right])

if __name__ == '__main__':
    s = Solution()
    nums = [3,4,5]
    print(s.findMin(nums))
    # print([i for i in nums[0:3]])
