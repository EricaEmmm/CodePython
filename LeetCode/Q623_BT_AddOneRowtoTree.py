# 在二叉树中增加一行
# 给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
# 将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。
# 如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
# 示例 1:
# 输入:
# 二叉树如下所示:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
# v = 1
# d = 2
# 输出:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5

from tool import TreeNode
import Q144_BT_BinaryTreePreorderTraversal

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def helper(root, v, d, level):
            if not root:
                return
            if level+1 == d:
                node_left = TreeNode(v)
                node_left.left = root.left
                root.left = node_left
                node_right = TreeNode(v)
                node_right.right = root.right
                root.right = node_right
                return
            helper(root.left, v, d, level+1)
            helper(root.right, v, d, level+1)
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        helper(root, v, d, 1)
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    # root.right = TreeNode(6)
    # root.right.left = TreeNode(5)
    out = Q144_BT_BinaryTreePreorderTraversal.Solution()
    print(out.preorderTraversal(s.addOneRow(root,1,3)))