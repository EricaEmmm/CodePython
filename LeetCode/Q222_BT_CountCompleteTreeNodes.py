# 给出一个完全二叉树，求出该树的节点个数。
# 说明：
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# 输出: 6

from tool import TreeNode

class Solution(object):
    # 法一：递归
    def countNodes1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.helper(root, res)
        return res[0]

    def helper(self, root, res):
        if root == None:
            return
        res[0] += 1
        self.helper(root.left, res)
        self.helper(root.right, res)

    # 法二：递归
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)

    # 法三：
    # 完全二叉树的高度可以直接通过不断地访问左子树获取
    # 判断左右子树的高度:
    # 如果相等说明左子树是满二叉树, 然后进一步判断右子树的节点数(最后一层最后出现的节点必然在右子树中)
    # 如果不等说明右子树是深度小于左子树的满二叉树, 然后进一步判断左子树的节点数(最后一层最后出现的节点必然在左子树中)
    def countNodes3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depthl = self.getDepth(root.left)
        depthr = self.getDepth(root.right)
        if depthl == depthr:        # 左子树是满二叉树, 右子树是完全二叉树
            return (1<<depthl) + self.countNodes3(root.right)
        else:                       # 右子树是深度小于左子树的满二叉树, 左子树是完全二叉树
            return (1<<depthr) + self.countNodes3(root.left)

    def getDepth(self, root):
        depth = 0
        while root != None:
            depth += 1
            root = root.left
        return depth

    def countNodes(self, root):
        return  self.countNodes3(root)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    print(s.countNodes(root))