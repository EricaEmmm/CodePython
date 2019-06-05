# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def OutputTree(self, tree):
    #     """
    #     :type tree: List[TreeNode]
    #     :rtype res: List[str]
    #     """
    #     if tree == None:
    #         return
    #     queue = []
    #     while()

    def OutputTreeFront(self, root, res):
        """
        先序遍历：根结点 ---> 左子树 ---> 右子树
        """
        if root == None:
            return
        res.append(root.val)
        self.OutputTreeFront(root.left, res)
        self.OutputTreeFront(root.right, res)

    def OutputTreeMiddle(self, root, res):
        """
        中序遍历：左子树---> 根结点 ---> 右子树
        """
        if root == None:
            return
        self.OutputTreeMiddle(root.left, res)
        res.append(root.val)
        self.OutputTreeMiddle(root.right, res)

    def OutputTreeRear(self, root, res):
        """
        后序遍历：左子树 ---> 右子树 ---> 根结点
        """
        if root == None:
            return
        self.OutputTreeRear(root.left, res)
        self.OutputTreeRear(root.right, res)
        res.append(root.val)

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
        return "[{}]".format(', '.join(serializedTreeNodes))


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def InputIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[Interval]
        """
        res = []
        for i in intervals:
            res.append(Interval(i[0],i[1]))
        return res

    def OutputIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[List[int]]
        """
        res = []
        for i in intervals:
            res.append([i.start, i.end])
        print(res)



if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # test = Interval()
    # test.OutputIntervals(test.InputIntervals(intervals))

    s = TreeNode(2)
    s.left = TreeNode(1)
    s.right = TreeNode(3)
    res = []
    s.OutputTreeLevel(s, res)
    print(res)