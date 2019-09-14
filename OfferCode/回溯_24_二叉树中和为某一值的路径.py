'''
二叉树中和为某一值的路径
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

from tool import TreeNode

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        res = []
        self.helper(root, res, [], expectNumber)
        res.sort(key=lambda x:len(x), reverse=True)
        return res

    def helper(self, root, res, path, expectNumber):
        path.append(root.val)
        expectNumber = expectNumber - root.val
        if expectNumber == 0:
            if not root.left and not root.right:
                res.append(path)
            return
        if root.left:
            self.helper(root.left, res, path[:], expectNumber)
        if root.right:
            self.helper(root.right, res, path[:], expectNumber)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.right = TreeNode(3)
    print(s.FindPath(root, 10))