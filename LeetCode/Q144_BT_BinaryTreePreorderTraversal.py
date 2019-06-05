# 二叉树的前序遍历
# 给定一个二叉树，返回它的 前序 遍历。
#
# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [1,2,3]

from tool import TreeNode

class Solution(object):
    # 法一：递归
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.helper(root, res)
        return res

    def helper(self, root, res):
        res.append(root.val)
        if root.left == None and root.right == None:
            return
        if root.left != None:
            self.helper(root.left, res)
        if root.right != None:
            self.helper(root.right, res)
    # 法二：迭代
    # 模拟系统栈，这种思路可以将任何递归算法改为为非递归
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        stack = []
        stack.append(root)
        while stack != []:
            tmp = stack[-1]
            res.append(tmp.val)         # 取根节点的值
            stack.pop()
            if tmp.right:
                stack.append(tmp.right) # 先压右节点
            if tmp.left:
                stack.append(tmp.left)  # 再压左节点
        return res

    def preorderTraversal(self, root):
        return self.preorderTraversal1(root)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(s.preorderTraversal(root))
    # stack = []
    # stack.append('3')
    # tmp = stack[0]
    # print(tmp)