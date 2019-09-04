'''
二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

from tool import TreeNode


class Solution(object):
    def maxDepth1(self, root):
        '''
        递归/DFS
        '''
        if not root:
            return 0
        return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1

    def maxDepth2(self, root):
        '''
        BFS
        '''
        if not root:
            return 0
        que = []
        que.append((root, 1))
        while que:
            cur, depth = que.pop(0)
            if cur.left != None: que.append((cur.left, depth+1))
            if cur.right != None: que.append((cur.right, depth+1))
        return depth

    def maxDepth(self, root):
        return self.maxDepth2(root)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.maxDepth(root))


