'''
二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        n = len(sequence)
        if n == 0: return False
        if n == 1: return True

        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1

        for j in range(i, n-1):
            if root > sequence[j]: return False

        left, right = True, True
        if len(sequence[:i]) > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if len(sequence[i:n-1]) > 0:
            right = self.VerifySquenceOfBST(sequence[i:n-1])
        return left and right

if __name__ == '__main__':
    s = Solution()
    sequence = [4,6,7,5]#[1,4,3,6,8,7,10]
    print('Yes') if s.VerifySquenceOfBST(sequence) else print('No')