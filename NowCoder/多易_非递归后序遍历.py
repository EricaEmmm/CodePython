# 用非递归方式实现二叉树后序遍历。
#
# 示例：
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# 输出: [5, 3, 3, 9, 2, 1]

from tool import TreeNode

def OutputTreeRear(self, root, res):
    if not root:
        return

    sta = []



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)