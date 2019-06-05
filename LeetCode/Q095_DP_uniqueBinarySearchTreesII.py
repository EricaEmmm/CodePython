# 不同的二叉搜索树 II
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

"""
对于[left, right]中的一点i，若要生成以i为根节点的BST，则有如下规律：
i左边的序列可以作为左子树结点，且左儿子可能有多个，所以有 left_nodes = dfs(left, i - 1);；
i右边的序列可以作为右子树结点，同上所以有 right_nodes = dfs(i + 1, right);；
产生的以当前i为根结点的BST（子）树有left_nodes.size() * right_nodes.size()个，遍历每种情况，即可生成以i为根节点的BST序列；
然后以for循环使得[left, right]中每个结点都能生成子树序列。
"""

from tool import TreeNode

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n:
            return self.dfs(1, n)
        else:
            return []

    def dfs(self, left, right):
        res = []
        if left > right:
            return [None]
        for i in range(left, right+1):
            left_nodes = self.dfs(left, i-1)
            right_nodes = self.dfs(i+1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    res.append(node)
        return res

    def OutputTreeLevel(self, root, res):
        """
        层次遍历
        """
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def treeNodeToString(self, root):
        if not root:
            return "[]"
        output = ""
        queue = [root]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output += "null, "
                continue

            output += str(node.val) + ", "
            queue.append(node.left)
            queue.append(node.right)
        return "[" + output[:-2] + "]"

    def treeNodeArrayToString(self, treeNodeArray):
        serializedTreeNodes = []
        for treeNode in treeNodeArray:
            serializedTreeNode = self.treeNodeToString(treeNode)
            serializedTreeNodes.append(serializedTreeNode)
        return "[{}]".format(',\n'.join(serializedTreeNodes))

if __name__ == '__main__':
    s = Solution()
    # for i in s.generateTrees(3):
    #     res = []
    #     s.OutputTreeLevel(i, res)
    #     print(res)
    print(s.treeNodeArrayToString(s.generateTrees(3)))
