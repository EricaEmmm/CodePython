# 树的子结构
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

from tool import TreeNode

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return False
        if not pRoot1:
            return False

        res = False
        # 如果当前两个树节点值相同
        if pRoot1.val == pRoot2.val:
            res = self.isSubtree(pRoot1, pRoot2)        # 判断树A中以R为根节点的子树是不是包含和树B一样的结构
        # 如果当前两个树节点值不同
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)  # A树的左节点中有没有
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2) # A树的右节点中有没有
        return res

    def isSubtree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val == root2.val:
            return self.isSubtree(root1.left, root2.left) and self.isSubtree(root1.right, root2.right)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    a = TreeNode(8)
    a.left = TreeNode(8)
    a.left.left = TreeNode(9)
    a.left.left.left = TreeNode(9)
    a.left.right = TreeNode(2)
    a.right = TreeNode(7)
    b = TreeNode(8)
    b.left = TreeNode(9)
    b.right = TreeNode(2)
    print(s.HasSubtree(a, b))

