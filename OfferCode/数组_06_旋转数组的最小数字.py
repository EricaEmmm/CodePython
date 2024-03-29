# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0

        left, right = 0, len(rotateArray)-1
        while left+1 < right:
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid
            elif rotateArray[mid] < rotateArray[left]:
                right = mid
        return min(rotateArray[left], rotateArray[right])


if __name__ == '__main__':
    s = Solution()
    rotateArray = [3,4,5,6,2]
    print(s.minNumberInRotateArray(rotateArray))