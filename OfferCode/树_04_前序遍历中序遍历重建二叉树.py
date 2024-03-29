# 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

from tool import TreeNode

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return
        root = TreeNode(pre[0])
        tinIndex = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:tinIndex+1], tin[:tinIndex])
        root.right = self.reConstructBinaryTree(pre[tinIndex+1:], tin[tinIndex+1:])
        return root


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
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    print(OutputTreeFront(s.reConstructBinaryTree(pre, tin)))