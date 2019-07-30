# 二叉树的镜像
# 题目描述
#     操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述:
# 二叉树的镜像定义：
# 源二叉树
#     	    8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9 11
# 镜像二叉树
#     	    8
#     	   /  \
#     	  10   6
#     	 / \  / \
#     	11 9 7  5

from tool import TreeNode

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)

def OutputTreeFront(root):
    """
    先序遍历：根结点 ---> 左子树 ---> 右子树
    """
    if root == None:
        return
    print(root.val)
    OutputTreeFront(root.left)
    OutputTreeFront(root.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    # root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)

    s.Mirror(root)
    OutputTreeFront(root)

