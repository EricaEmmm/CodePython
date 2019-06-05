# 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
# 输入: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \
#      3   1
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
# 输入: [3,4,5,1,3,null,1]
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

from tool import TreeNode

# 动态规划
# DP状态定义：helper(root, 0)表示不抢root节点可获得最大值，helper(root, 1)表示抢root节点可获得最大值
# DP状态方程：helper(root, 0) = max( helper(root.left, 0), helper(root.left, 1) ) + max( helper(root.right, 0), helper(root.right, 1) )
#             helper(root, 1) = root.val + helper(root.left, 0) + helper(root.right, 0)

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        storage_0 = dict()  # 不添加记忆，则会超时
        storage_1 = dict()

        def helper(root, take):
            if not root:
                return 0
            if take:
                if root.left not in storage_0:
                    storage_0[root.left] = helper(root.left, 0)
                if root.right not in storage_0:
                    storage_0[root.right] = helper(root.right, 0)
                return root.val + storage_0[root.left] + storage_0[root.right]
            else:
                if root.left not in storage_0:
                    storage_0[root.left] = helper(root.left, 0)
                if root.right not in storage_0:
                    storage_0[root.right] = helper(root.right, 0)
                if root.left not in storage_1:
                    storage_1[root.left] = helper(root.left, 1)
                if root.right not in storage_1:
                    storage_1[root.right] = helper(root.right, 1)
                return max( storage_0[root.left], storage_1[root.left] ) + max( storage_0[root.right], storage_1[root.right] )

        return max(helper(root, 0), helper(root, 1))

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(1)
    print(s.rob(root))