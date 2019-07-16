# 路径总和 II
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from tool import TreeNode

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        self.getPath(root, sum, [], res)
        return res

    def getPath(self, root, sums, tmp, res):
        tmp.append(root.val)
        if (root.left == None) and (root.right == None):
            if sum(tmp) == sums:
                res.append(tmp)
            return
        if root.left != None:
            self.getPath(root.left, sums, tmp[:], res)  # 传入的tmp是快照
        if root.right != None:
            self.getPath(root.right, sums, tmp[:], res)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(s.pathSum(root, 22))
