# 从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7


# 前序 / 后序 + 中序序列可以唯一确定一棵二叉树
#   后序遍历：左-右-根
#   中序遍历：左-根-右
# 1.后序中最后肯定是根结点，我们可以据此找到中序中根结点的位置；
# 2.中序中根结点左边就是左子树结点，右边就是右子树结点；
# 3.进一步，找到左子树、右子树在后序中的位置；
# 4.划分子问题：构建左子树、右子树。

from tool import TreeNode

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])      # 后序中最后肯定是根结点
        root_index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])    #左闭右开
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
        return root

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
        return "[{}]".format(', '.join(serializedTreeNodes))

if __name__ == '__main__':
    s = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(s.treeNodeToString(s.buildTree(inorder, postorder)))
    # print(inorder[:2-1])