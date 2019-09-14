'''
二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

from tool import TreeNode

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        que = self.helper(pRootOfTree)
        # 将后序遍历的节点连成双向链表
        for i in range(1, len(que)):
            que[i-1].right = que[i]
            if que[i]:
                que[i].left = que[i-1]
        return que[0]

    # 后序遍历存储节点
    def helper(self, root):
        que = []
        sta = []
        cur = root
        while cur or sta:
            while cur:
                sta.append(cur)
                cur = cur.left
            cur = sta.pop()
            que.append(cur)
            cur = cur.right
        return que

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(s.Convert(root))