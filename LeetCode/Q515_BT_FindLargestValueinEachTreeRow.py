# 在每个树行中找最大值
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# 输出: [1, 3, 9]

from tool import TreeNode

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue, res = [], []         # 队列用于层次遍历，记录节点及其所属层
        queue.append([root, 1])

        while queue:                # 层次遍历
            tmp = queue.pop(0)
            node = tmp[0]
            if len(res) < tmp[1]:   # 该节点属于新层，添加节点值
                res.append(node.val)
            else:                   # 更新该层最大节点值
                res[tmp[1]-1] = max(res[tmp[1]-1], node.val)
            if node.left != None:
                queue.append([node.left, tmp[1]+1])
            if node.right != None:
                queue.append([node.right, tmp[1]+1])
        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    print(s.largestValues(root))

    # t = dict()
    # t[3] = 0
    # t[4] = 1
    # t[5] = 1
    # res = [0, 0]
    # for i in range(len(res)):
    #     res[i] = max(k for k,v in t.items() if v == i)
    # print(res)
