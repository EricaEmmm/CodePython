'''
从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
from tool import TreeNode

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        que = [root]
        while que:
            cur = que.pop(0)
            res.append(cur.val)
            if cur.left: que.append(cur.left)
            if cur.right: que.append(cur.right)
        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(s.PrintFromTopToBottom(root))
